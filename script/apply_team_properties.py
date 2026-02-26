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

    # We need to read the mapping file first to extract allowed values
    try:
        with open(MAPPING_FILE, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"Error reading Markdown table: {e}")
        sys.exit(1)

    distinct_teams = set()
    repo_data = {}

    for line in lines:
        if line.strip().startswith('|') and 'Repository Name' not in line and '---' not in line:
            parts = line.split('|')
            if len(parts) >= 4:
                repo_name = parts[1].strip().replace('`', '')
                team_name = parts[2].strip()

                if not repo_name:
                    continue

                if "/" in repo_name:
                    repo_name = repo_name.split("/")[-1]
                
                if team_name:
                    # Handle comma-separated teams if any exist in the field
                    current_teams = [t.strip() for t in team_name.split(',')]
                    distinct_teams.update(current_teams)

                    if repo_name not in repo_data:
                        repo_data[repo_name] = {"teams": []}
                        
                    for t in current_teams:
                        if t and t not in repo_data[repo_name]["teams"]:
                            repo_data[repo_name]["teams"].append(t)
                            
    print(f"Loaded {len(distinct_teams)} distinct team values for the Custom Property.")
    
    # Make sure 'Team' property exists in the org before attempting to patch repos
    print("Checking/Creating 'Team' custom property at Org level...")
    if not DRY_RUN:
        prop_payload = {
            "value_type": "multi_select",
            "required": False,
            "description": "The teams responsible for this repository.",
            "allowed_values": sorted(list(distinct_teams))
        }
        with open("team_prop_payload.json", "w") as f:
            json.dump(prop_payload, f)
        run_gh_command(["api", "--method", "PUT", "-H", "Accept: application/vnd.github+json", f"orgs/{ORG_NAME}/properties/schema/Team", "--input", "team_prop_payload.json"])
        if os.path.exists("team_prop_payload.json"):
            os.remove("team_prop_payload.json")

    # Parsing is now handled in the block above

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
        # For multi_select, the value must be a JSON array of strings
        payload = {
            "properties": [
                {
                    "property_name": "Team",
                    "value": teams
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
            print(f"  [SUCCESS] Assigned teams: {teams}")
            success_count += 1
             
        if not DRY_RUN:
            time.sleep(1.5)

    if os.path.exists("payload.json"):
        os.remove("payload.json")
        
    print("-" * 40)
    print(f"Property Sync Completed: {success_count} succeeded, {fail_count} failed.")

if __name__ == "__main__":
    main()
