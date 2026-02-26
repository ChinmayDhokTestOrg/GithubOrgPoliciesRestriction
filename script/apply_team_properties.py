import subprocess
import json
import time
import os
import sys

ORG_NAME = os.environ.get("ORGANIZATION")
MAPPING_FILE = "doc/ONLINESALES_AI_REPO_MAPPING.md"
DRY_RUN = os.environ.get("DRY_RUN", "false").lower() == "true"

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

    if not os.path.exists(MAPPING_FILE):
        print(f"[INFO] Skipping property assignment: '{MAPPING_FILE}' not found.")
        sys.exit(0)

    print(f"Loading organization mapping data for '{ORG_NAME}'...")
    if DRY_RUN:
        print("*** DRY RUN MODE ENABLED: No changes will be applied to GitHub ***")

    # Make sure 'Team' property exists in the org before attempting to patch repos
    print("Checking/Creating 'Team' custom property at Org level...")
    if not DRY_RUN:
        prop_payload = {
            "value_type": "string",
            "required": False,
            "description": "The team responsible for this repository."
        }
        with open("team_prop_payload.json", "w") as f:
            json.dump(prop_payload, f)
        run_gh_command(["api", "--method", "PUT", "-H", "Accept: application/vnd.github+json", f"orgs/{ORG_NAME}/properties/schema/Team", "--input", "team_prop_payload.json"])
        if os.path.exists("team_prop_payload.json"):
            os.remove("team_prop_payload.json")

    repo_data = {}
    try:
        with open(MAPPING_FILE, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                if line.strip().startswith('|') and 'Repository Name' not in line and '---' not in line:
                    parts = line.split('|')
                    if len(parts) >= 4:
                        repo_name = parts[1].strip().replace('`', '')
                        team_name = parts[2].strip()
                        role_name = parts[3].strip()

                        if not repo_name:
                            continue

                        # Strip potential org prefixes
                        if "/" in repo_name:
                            repo_name = repo_name.split("/")[-1]

                        if repo_name not in repo_data:
                            repo_data[repo_name] = {"teams": []}

                        # If user gave a team, map it
                        if team_name and team_name not in repo_data[repo_name]["teams"]:
                            repo_data[repo_name]["teams"].append(team_name)
    except Exception as e:
        print(f"Error reading and parsing Markdown table: {e}")
        sys.exit(1)

    print(f"Resolved mapping for {len(repo_data)} repositories.")
    print("-" * 40)

    success_count = 0
    fail_count = 0

    for repo, data in repo_data.items():
        teams = data["teams"]
        
        # We only assign if there's a team specified in the mapping table
        if not teams:
            continue
            
        print(f"Syncing [Team] property for repository: {repo}")
        
        # GitHub requires the value to be a list of strings for single_select and an exact string or list based on definition
        # If 'Team' is defined as a string, we might want to just set it to the first team or join them.
        # Assuming we just set the exact string provided.
        team_value = teams[0] if len(teams) == 1 else ", ".join(teams)
        
        payload = {
            "properties": [
                {
                    "property_name": "Team",
                    "value": team_value
                }
            ]
        }
        
        if DRY_RUN:
            print(f"  [DRY RUN] Would assign property to {repo}:")
            print(json.dumps(payload, indent=2))
            success_count += 1
            continue
             
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
            print(f"  [SUCCESS] Assigned team: {team_value}")
            success_count += 1
             
        if not DRY_RUN:
            time.sleep(1.5)

    if os.path.exists("payload.json"):
        os.remove("payload.json")
        
    print("-" * 40)
    print(f"Property Sync Completed: {success_count} succeeded, {fail_count} failed.")

if __name__ == "__main__":
    main()
