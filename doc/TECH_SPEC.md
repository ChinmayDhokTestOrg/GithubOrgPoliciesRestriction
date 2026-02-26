# Technical Specification: GitHub Governance Automation

## 1. Overview
The GitHub Governance Automation project consists of a suite of Python scripts and GitHub Actions workflows designed to enforce organizational policies across a large number of repositories. The primary goals are to standardize branch protection rules and automate the assignment of team access properties.

## 2. Architecture
The solution relies on the GitHub CLI (`gh`) and the GitHub REST API to interact with the organization's resources. Python is used as the scripting language for its data manipulation capabilities (specifically using `pandas` for CSV parsing).

### Components
- **Scripts:**
  - `create_org_properties.sh`: Org-level custom property schema definitions.
  - `create_org_ruleset.sh`: Applies branch protections across the org via a GitHub Organization Ruleset.
  - `apply_team_properties.py`: Maps repository access to GitHub Custom Properties (`Team`).
- **Data Sources:**
  - `github-full-inventory.csv`: A comprehensive list of all repositories in the organization, including metadata like branch count and primary language.
  - `team-access-by-repo.csv`: A mapping of repositories to teams and their access roles (`admin`, `write`, `maintain`).
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
  1. Parses `team-access-by-repo.csv`.
  2. Filters for roles that imply significant access (`admin`, `write`, `maintain`).
  3. Aggregates the teams associated with each repository.
  4. Uses the GitHub API (`PATCH /repos/{owner}/{repo}/properties/values`) to update the "Team" property with an array of team names.

## 4. Error Handling and Rate Limiting
- **Subprocess Checks:** Calls to the `gh` CLI use `check=True` where appropriate, or catch `subprocess.CalledProcessError` to gracefully handle API errors (e.g., 404s for missing branches).
- **Rate Limiting:** Both scripts incorporate `time.sleep()` between API calls (1.0s to 1.5s) to mitigate secondary API rate limits imposed by GitHub.

## 5. Security Considerations
- The scripts rely on the environment having a valid, authenticated GitHub CLI session (`gh auth login`).
- Custom API endpoints are constructed dynamically. Careful validation of repository names from the CSV is implicit, but assuming the CSV is generated from a trusted source.

## 6. Future Enhancements
- Implement parallel processing (with careful rate limit management) to speed up execution across 400+ repositories.
- Add robust logging instead of standard `print` statements.
