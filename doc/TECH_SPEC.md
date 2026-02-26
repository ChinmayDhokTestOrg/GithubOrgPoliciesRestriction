# Technical Specification: GitHub Governance Automation

## 1. Overview
The GitHub Governance Automation project consists of a suite of Python scripts and GitHub Actions workflows designed to enforce organizational policies across a large number of repositories. The primary goals are to standardize branch protection rules and automate the assignment of team access properties.

## 2. Architecture
The solution relies on the GitHub CLI (`gh`) and the GitHub REST API to interact with the organization's resources. Python is used as the scripting language for its data manipulation capabilities (specifically using `pandas` for CSV parsing).

### Components
- **Scripts:**
  - `enforce_branch_rules.py`: Applies branch protection rules to `stage` and production (`release`/`main`) branches.
  - `apply_team_properties.py`: Maps repository access to GitHub Custom Properties (`Team`).
- **Data Sources:**
  - `github-full-inventory.csv`: A comprehensive list of all repositories in the organization, including metadata like branch count and primary language.
  - `team-access-by-repo.csv`: A mapping of repositories to teams and their access roles (`admin`, `write`, `maintain`).
- **Workflows:**
  - `github-governance-sync.yml` (Hypothetical/Planned): CI/CD pipeline to run these scripts on a schedule or manual trigger.

## 3. Detailed Design

### 3.1 Branch Protection Enforcer (`enforce_branch_rules.py`)
This script reads the repository inventory and applies specific protection rules based on the branch name.

- **Dependencies:** `pandas`, `subprocess`, `json`, `os`, `sys`, `time`
- **Input:** `github-full-inventory.csv`
- **Logic:**
  1. Parses the CSV to extract a unique list of repositories.
  2. Iterates through each repository.
  3. Checks for the existence of a `stage` branch. If found, applies rules:
     - Require Pull Request
     - 2 Approvals required
     - Enforce Admins
     - No Force Pushes
     - No Deletions
  4. Checks for the existence of `release` or `main` (prioritizing `release`). If found, applies similar rules, but includes a specific status check context: `Verify Source Branch is Stage` (if applicable/configured).

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
