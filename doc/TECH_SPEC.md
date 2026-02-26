# Technical Specification: GitHub Governance Automation

## 1. Overview
The GitHub Governance Automation project consists of a suite of Python scripts and GitHub Actions workflows designed to enforce organizational policies across a large number of repositories. The primary goals are to standardize branch protection rules and automate the assignment of team access properties.

## 2. Architecture
The solution relies entirely on the GitHub REST API and GitHub CLI (`gh`) to provision Organization-Level rulesets and metadata schemas across the organization's repositories. Python is used purely as a data manipulation utility (using the built-in `csv` module) for applying CSV maps to those custom properties.

### Components
- **Scripts:**
  - `create_org_properties.sh`: Org-level custom property schema definitions.
  - `create_org_ruleset.sh`: Applies branch protections across the org via a GitHub Organization Ruleset.
  - `apply_team_properties.py`: Maps repository access to GitHub Custom Properties (`Team`).
- **Data Sources:**
  - `script/team-access-by-repo.csv`: An optional mapping of repositories to teams and their access roles. A blank template is provided as `team-access-by-repo.template.csv`.
- **Workflows:**
  - `github-governance-sync.yml` (Hypothetical/Planned): CI/CD pipeline to run these scripts on a schedule or manual trigger.

## 3. Detailed Design

### 3.1 Organization Ruleset Creator (`create_org_ruleset.sh`)
This bash script uses the `gh api` to create a singular organization-level ruleset that targets all repositories (`~ALL`) and enforces required pull requests and approvals on `stage`, `release`, `main`, and `master` branches. This eliminates the need for repository-by-repository looping for branch enforcement.

### 3.2 Team Property Synchronizer (`apply_team_properties.py`)
This script translates team access rights into a GitHub Custom Property named "Team" on each repository.

- **Dependencies:** `pandas`, `subprocess`, `json`, `os`, `sys`, `time`
- **Input:** `github-full-inventory.csv`, `team-access-by-repo.csv`
- **Logic:**
  1. Parses the optional `team-access-by-repo.csv` (if present).
  2. Filters for roles that imply significant access (`admin`, `write`, `maintain`).
  3. Drops the `onlinesales-ai/` prefix (if included) so it properly addresses the repo endpoint.
  4. Aggregates the teams associated with each repository.
  5. Uses the GitHub API (`PUT /orgs/{owner}/properties/values`) or sequential patch calls to update the "Team" property.

## 4. Error Handling
- **Subprocess Checks:** Calls to the `gh` CLI use `check=True` where appropriate, or catch `subprocess.CalledProcessError` to gracefully handle API errors.
- **Missing Data Mitigation:** If a user runs the workflow on a new organization but forgets to upload a CSV mapping, the workflow prints a warning and gracefully exits the assignment step without crashing the pipeline, allowing the branch rules to still deploy.

## 5. Security Considerations
- The scripts rely on the environment having a valid, authenticated GitHub CLI session (`gh auth login`).
- Custom API endpoints are constructed dynamically. Careful validation of repository names from the CSV is implicit, but assuming the CSV is generated from a trusted source.

- **Actions Secrets:** The workflow expects an `ORG_ADMIN_TOKEN` secret in the repository running the code.

## 6. Future Enhancements
- Automate the parsing of Markdown tables (e.g., `ONLINESALES_AI_REPO_MAPPING.md`) back into CSV format via a GitHub Action to eliminate manual conversion steps for managers.
