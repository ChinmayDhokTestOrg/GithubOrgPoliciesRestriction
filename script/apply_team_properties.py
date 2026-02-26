import pandas as pd
import subprocess
import json
import time
import os
import sys

ORG_NAME = os.environ.get("ORGANIZATION", "ChinmayDhokTestOrg")
INVENTORY_FILE = ".github/scripts/github-full-inventory.csv"
ACCESS_FILE = ".github/scripts/team-access-by-repo.csv"

def run_gh_command(args):
    """Executes a gh CLI command and returns stdout and stderr."""
    try:
        result = subprocess.run(["gh"] + args, capture_output=True, text=True, check=True)
        return result.stdout.strip(), None
    except subprocess.CalledProcessError as e:
        return None, e.stderr.strip()

def main():
    if not os.path.exists(ACCESS_FILE) or not os.path.exists(INVENTORY_FILE):
        print(f"Error: Missing CSV files. Please ensure '{INVENTORY_FILE}' and '{ACCESS_FILE}' exist.")
        sys.exit(1)

    print(f"Loading organization mapping data for '{ORG_NAME}'...")
    
    try:
        access_df = pd.read_csv(ACCESS_FILE)
        
        # Standardize column extraction based on reasonable expectations of CSV dumps.
        # Ensure we capture 'role' if present to filter only by Write/Admin/Maintain
        eligible_roles = ['admin', 'write', 'maintain']
        
        columns = [col.lower() for col in access_df.columns]
        
        repo_col = next((col for col in access_df.columns if 'repo' in col.lower()), access_df.columns[0])
        team_col = next((col for col in access_df.columns if 'team' in col.lower()), access_df.columns[1])
        role_col = next((col for col in access_df.columns if 'role' in col.lower()), None)
        
        if role_col:
            access_df[role_col] = access_df[role_col].astype(str).str.lower().str.strip()
            access_df = access_df[access_df[role_col].isin(eligible_roles)]
            
        repo_teams = {}
        
        for _, row in access_df.iterrows():
            repo = str(row[repo_col]).strip()
            team = str(row[team_col]).strip()
            if repo and team and str(team).lower() != 'nan':
                if repo not in repo_teams:
                    repo_teams[repo] = []
                if team not in repo_teams[repo]:
                    repo_teams[repo].append(team)
            
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
