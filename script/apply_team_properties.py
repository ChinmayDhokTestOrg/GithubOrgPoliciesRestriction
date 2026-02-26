import subprocess
import json
import time
import os
import sys
import csv

ORG_NAME = os.environ.get("ORGANIZATION")
INVENTORY_FILE = "script/github-full-inventory.csv"
ACCESS_FILE = "script/team-access-by-repo.csv"

def run_gh_command(args):
    """Executes a gh CLI command and returns stdout and stderr."""
    try:
        result = subprocess.run(["gh"] + args, capture_output=True, text=True, check=True)
        return result.stdout.strip(), None
    except subprocess.CalledProcessError as e:
        return None, e.stderr.strip()

def main():
    if not ORG_NAME:
        print("Error: ORGANIZATION environment variable is required.")
        sys.exit(1)

    if not os.path.exists(ACCESS_FILE):
        print(f"[INFO] Skipping Team assignment: '{ACCESS_FILE}' not found.")
        print("To automatically map teams to repositories, provide a CSV file with 'repo', 'team', and 'role' columns.")
        sys.exit(0) # Exit peacefully!

    print(f"Loading organization mapping data for '{ORG_NAME}'...")
    print(f"Note: Ensure the Custom Property 'Team' is created in the Org Settings first.")
    # Attempt to create the 'Team' property at the org level if it doesn't exist.
    # We swallow errors here in case it already exists.
    try:
        prop_payload = {
            "value_type": "string",
            "required": False,
            "description": "The team responsible for this repository."
        }
        with open("prop_payload.json", "w") as f:
            json.dump(prop_payload, f)
        run_gh_command(["api", "--method", "PUT", "-H", "Accept: application/vnd.github+json", f"orgs/{ORG_NAME}/properties/schema/Team", "--input", "prop_payload.json"])
        if os.path.exists("prop_payload.json"):
            os.remove("prop_payload.json")
    except Exception as e:
        pass
    
    try:
        # Load CSV using standard library
        repo_teams = {}
        with open(ACCESS_FILE, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                repo_name = row.get('repo', '').strip()
                team_name = row.get('team', '').strip()
                role_name = row.get('role', '').strip()

                if not repo_name or not team_name:
                    continue

                # Strip potential org prefixes
                if "/" in repo_name:
                    repo_name = repo_name.split("/")[-1]

                # Only map if the role implies significant access
                if role_name.lower() in ['admin', 'write', 'maintain']:
                    if repo_name not in repo_teams:
                        repo_teams[repo_name] = []
                    if team_name not in repo_teams[repo_name]:
                        repo_teams[repo_name].append(team_name)
    except Exception as e:
        print(f"Error reading and parsing CSVs: {e}")
        sys.exit(1)

    print(f"Resolved mapping for {len(repo_teams)} repositories.")
    print("-" * 40)

    success_count = 0
    fail_count = 0

    for repo, teams in repo_teams.items():
        print(f"Syncing [Team] property for repository: {repo}")
        
        # Payload format for GitHub REST API PATCH /repos/{owner}/{repo}/properties/values
        payload = {
            "properties": [
                {
                    "property_name": "Team",
                    "value": teams
                }
            ]
        }
        
        with open("payload.json", "w") as f:
            json.dump(payload, f)
            
        endpoint = f"repos/{ORG_NAME}/{repo}/properties/values"
        stdout, stderr = run_gh_command([
            "api", 
            "--method", "PATCH", 
            "-H", "Accept: application/vnd.github+json", 
            endpoint, 
            "--input", "payload.json"
        ])
        
        if stderr:
             print(f"  [ERROR] Failed to map property on '{repo}': {stderr}")
             fail_count += 1
        else:
             print(f"  [SUCCESS] Assigned teams: {teams}")
             success_count += 1
             
        # Delay to prevent API rate limiting
        time.sleep(1.5)

    if os.path.exists("payload.json"):
        os.remove("payload.json")
        
    print("-" * 40)
    print(f"Property Sync Completed: {success_count} succeeded, {fail_count} failed.")

if __name__ == "__main__":
    main()
