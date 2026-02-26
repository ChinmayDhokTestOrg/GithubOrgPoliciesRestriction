# GitHub Org Policies and Restriction

This repository contains scripts and configurations for automating governance policies across a GitHub Organization. It ensures that standard rules and access controls are applied consistently without manual intervention.

## Quick Links

- [Technical Specification](TECH_SPEC.md): A detailed overview of the script logic and API integration.
- [Deployment Plan](DEPLOYMENT_PLAN.md): Instructions for running the tools locally or in production.
- [Wiki Outline](WIKI.md): Recommended structure for a team-facing documentation wiki.

## Core Features

1.  **Branch Protection Enforcement:** Ensures that `stage` and high-level branches (`main` or `release`) have strict pull request reviews, status checks, and access rules (via `enforce_branch_rules.py`).
2.  **Team Property Synchronization:** Automatically assigns the GitHub Custom Property (`Team`) to repositories based on CSV access mappings (via `apply_team_properties.py`).

## Prerequisites

- **Authentication:** `gh auth login` with appropriate scopes (`Administration`, `Custom properties`).
- **Data Files:** Ensure `github-full-inventory.csv` and `team-access-by-repo.csv` are present in `.github/scripts/`.

## Usage

Example execution for applying team properties:
```bash
export ORGANIZATION="YourTestOrgName"
python .github/scripts/apply_team_properties.py
```
