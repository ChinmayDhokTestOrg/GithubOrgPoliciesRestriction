import pandas as pd
import subprocess
import json
import time
import os
import sys

ORG_NAME = os.environ.get("ORGANIZATION", "ChinmayDhokTestOrg")
INVENTORY_FILE = "script/github-full-inventory.csv"

def run_gh_command(args):
    """Executes a gh CLI command and returns stdout and stderr."""
    try:
        result = subprocess.run(["gh"] + args, capture_output=True, text=True, check=True)
        return result.stdout.strip(), None
    except subprocess.CalledProcessError as e:
        return None, e.stderr.strip()

def check_branch_exists(repo, branch):
    """Checks if a branch exists via GitHub API lookup."""
    endpoint = f"repos/{ORG_NAME}/{repo}/branches/{branch}"
    stdout, stderr = run_gh_command(["api", endpoint])
    return stderr is None

def apply_protection(repo, branch, rules_payload):
    """Applies a branch protection configuration via GitHub API."""
    print(f"  > Setting protection for branch: '{branch}'...")
    
    with open("rules_payload.json", "w") as f:
        json.dump(rules_payload, f)
        
    endpoint = f"repos/{ORG_NAME}/{repo}/branches/{branch}/protection"
    stdout, stderr = run_gh_command([
        "api", 
        "--method", "PUT", 
        "-H", "Accept: application/vnd.github+json", 
        endpoint, 
        "--input", "rules_payload.json"
    ])
    
    if stderr:
        if "404" in stderr or "Not Found" in stderr:
            print(f"    [WARN] Branch or repo not found, or unauthorized (404).")
        else:
            print(f"    [ERROR] Failed: {stderr}")
    else:
        print(f"    [SUCCESS] Rules applied to '{branch}'.")

def main():
    if not os.path.exists(INVENTORY_FILE):
        print(f"Error: Inventory file not found: {INVENTORY_FILE}")
        sys.exit(1)

    try:
        inventory_df = pd.read_csv(INVENTORY_FILE)
        # Attempt to grab the repo column
        repo_col = next((col for col in inventory_df.columns if 'repo' in col.lower()), inventory_df.columns[0])
        repos = inventory_df[repo_col].dropna().unique().tolist()
    except Exception as e:
        print(f"Error reading inventory CSV: {e}")
        sys.exit(1)

    print(f"Loaded {len(repos)} repositories from inventory to evaluate in '{ORG_NAME}'.")
    print("-" * 50)

    # RULE CONFIGURATIONS

    # stage branch: Require PR, 2 approvals (configured as 1 for Test org), CI checks, no direct pushes.
    stage_rules = {
        "required_status_checks": {
            "strict": True,
            "contexts": [] # Expand with checks like "build", "test" as needed
        },
        "enforce_admins": True,
        "required_pull_request_reviews": {
            "dismiss_stale_reviews": True,
            "require_code_owner_reviews": False,
            "required_approving_review_count": 2
        },
        "restrictions": None,
        "allow_force_pushes": False,
        "allow_deletions": False
    }

    # release/main branch: Require PR, 1 approval, Verify Source CI check, no direct pushes.
    release_rules = {
        "required_status_checks": {
             "strict": True,
             "contexts": ["Verify Source Branch is Stage"] # Bound to the PR Blocker check name
        },
        "enforce_admins": True,
        "required_pull_request_reviews": {
            "dismiss_stale_reviews": True,
            "require_code_owner_reviews": False,
            "required_approving_review_count": 2
        },
        "restrictions": None,
        "allow_force_pushes": False,
        "allow_deletions": False
    }

    for repo in repos:
        repo = str(repo).strip()
        print(f"[{repo}]")
        
        # 1. Evaluate Stage Branch
        if check_branch_exists(repo, "stage"):
            apply_protection(repo, "stage", stage_rules)
        else:
            print(f"  > [INFO] 'stage' branch does not exist. Skipping.")
            
        time.sleep(1.0) # Rate limiting
            
        # 2. Evaluate Release/Main/Master Branch
        active_prod_branch = None
        if check_branch_exists(repo, "release"):
            active_prod_branch = "release"
        elif check_branch_exists(repo, "main"):
            active_prod_branch = "main"
        elif check_branch_exists(repo, "master"):
            active_prod_branch = "master"
            
        if active_prod_branch:
             apply_protection(repo, active_prod_branch, release_rules)
        else:
             print(f"  > [INFO] Neither 'release' nor 'main' branches exist. Skipping.")

        time.sleep(1.0) # Rate limiting
        print("")

    if os.path.exists("rules_payload.json"):
        os.remove("rules_payload.json")
        
    print("-" * 50)
    print("Branch protection sync completed.")

if __name__ == "__main__":
    main()
