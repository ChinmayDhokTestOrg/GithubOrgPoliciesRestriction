# Deployment Plan: GitHub Governance Automation

This document outlines the steps required to deploy and run the GitHub Governance Automation scripts across the organization.

## Prerequisites

1.  **Authentication:** The scripts require a GitHub Personal Access Token (PAT) or a GitHub App token with the following scopes/permissions across the organization's repositories:
    *   `Administration` (Read/Write) - for branch protection rules.
    *   `Custom properties` (Read/Write) - for assigning team properties.
    *   `Metadata` (Read-only) - to verify branch existence.
2.  **Environment:**
    *   Python 3.8+
    *   GitHub CLI (`gh`) installed and authenticated.
    *   Python `pandas` library (`pip install pandas`).
3.  **Data Files:**
    *   `script/github-full-inventory.csv`
    *   `script/team-access-by-repo.csv`

## Deployment Strategy

### Phase 1: Local Testing & Validation (Dry Run)
*Status: Completed during development.*

1.  Ensure `.csv` files are placed in `script/`.
2.  Set the target organization environment variable:
    ```bash
    export ORGANIZATION="YourTestOrgName"
    ```
3.  Authenticate GitHub CLI:
    ```bash
    gh auth login
    ```
4.  Execute scripts locally to monitor output and verify API calls function as expected without rate limiting crashing the process.

### Phase 2: Production Execution (Repository by Repository)
*Status: Pending execution.*

Due to the volume of repositories (412+), it is recommended to run the scripts from a local machine or a dedicated runner where standard output can be easily monitored and resumed if interrupted.

1.  **Apply Team Properties:**
    ```bash
    python script/apply_team_properties.py
    ```
    *Estimated time: ~10-15 minutes (due to intentional API delays).*
    *Validation: Spot-check 3-5 repositories in the GitHub UI to ensure the `Team` custom property is populated correctly.*

2.  **Enforce Branch Protection:**
    ```bash
    python script/enforce_branch_rules.py
    ```
    *Estimated time: ~15-20 minutes.*
    *Validation: Spot-check a repository with a `stage` and a `main`/`release` branch to verify the 2-approval requirement and status checks are active.*

### Phase 3: Automation via CI/CD (Future State)
To ensure continuous compliance, these scripts should be integrated into a scheduled GitHub Actions workflow.

1.  Create a secret `ORG_ADMIN_TOKEN` at the organization level containing a PAT with the necessary scopes.
2.  Enable the `.github/workflows/github-governance-sync.yml` workflow (ensure it is configured to trigger on a `schedule` or `workflow_dispatch`).
3.  Monitor workflow runs for failures caused by updated repository inventories or API changes.

## Rollback Plan
If incorrect rules or properties are applied:
1.  **Properties:** Run a modified version of `apply_team_properties.py` that sends an empty array `[]` to the properties endpoint to clear the assignments.
2.  **Branch Rules:** Branch protection rules cannot easily be bulk-deleted without storing the internal Rule IDs. A rollback would require manual intervention or a script specifically designed to target and evaluate the `DELETE /repos/{owner}/{repo}/branches/{branch}/protection` endpoint. Therefore, thoroughly review the CSV data prior to Phase 2.
