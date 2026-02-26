# Deployment Plan: GitHub Governance Automation

This document outlines the steps required to deploy and run the GitHub Governance Automation scripts across the organization.

## Prerequisites

1.  **Authentication:** The organization owner must create a GitHub Personal Access Token (PAT) with the following scopes/permissions across the organization's repositories:
    *   **Classic PAT:** `admin:org`, `repo`
    *   **Fine-Grained PAT (Org Permissions):** `Administration` (Read/Write), `Custom properties` (Read/Write)
2.  **Environment:**
    *   No local environment is strictly required, as the governance synchronization runs natively within GitHub Actions.
3.  **Data Files (Optional):**
    *   If you intend to map specific teams and properties to repositories, you must provide the mapping in `doc/ONLINESALES_AI_REPO_MAPPING.md`. If not provided or empty, the sync skips assignment.

## Deployment Strategy

### Phase 1: Local Testing & Validation (Dry Run)
*Status: Deprecated.* 

With the shift to Organization-Level APIs, local dry-running is discouraged. Properties and Rulesets are provisioned globally. To test the workflow, execute it against a sandbox/test organization first.

### Phase 2: Production Execution (GitHub Actions)
*Status: Active Strategy.*

Due to the volume of repositories (412+), it is recommended to run the automation directly via GitHub Actions to avoid local API rate limits or connection drops.

1.  **Create Organization Property Schemas:**
    *   This is handled automatically by the `GitHub Governance Organization Sync` workflow executing `script/create_org_properties.sh`.

2.  **Apply Team Properties to Repositories:**
    *   This is handled automatically by the workflow executing `script/apply_team_properties.py`.
    *   *Validation: Spot-check 3-5 repositories in the GitHub UI to ensure the `Team` custom property is populated correctly.*

3.  **Enforce Branch Protection (Organization Ruleset):**
    *   This is handled automatically by the workflow executing `script/create_org_ruleset.sh`.
    *   *Validation: Check your Organization Settings -> Rules -> Rulesets to verify the "Enforce Standard Branch Flows" ruleset is active.*

### Phase 3: Continuous Automation
To ensure continuous compliance across newly created repositories, this Action can be triggered manually or on a schedule. 

1.  Ensure the repository secret `ORG_ADMIN_TOKEN` exists and has the necessary organizational scopes.
2.  Navigate to the **Actions** tab.
3.  Select the **GitHub Governance Organization Sync** workflow and run it with your target organization's name to instantly synchronize all rules and properties.

## Rollback Plan
If incorrect rules or properties are applied:
1.  **Properties:** Run a modified version of `apply_team_properties.py` that sends an empty array `[]` to the properties endpoint to clear the assignments.
2.  **Branch Rules:** Because we use an Organization Ruleset, rollback is trivial. Simply navigate to Organization Settings -> Rules -> Rulesets and disable or delete the "Enforce Standard Branch Flows" ruleset.
