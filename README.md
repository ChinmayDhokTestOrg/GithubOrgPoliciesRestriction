# GitHub Org Policies and Restriction

This repository contains scripts and configurations for automating governance policies across a GitHub Organization. It ensures that standard rules and access controls are applied consistently without manual intervention.

## Quick Links

- [Technical Specification](doc/TECH_SPEC.md): A detailed overview of the script logic and API integration.
- [Deployment Plan](doc/DEPLOYMENT_PLAN.md): Instructions for running the tools locally or in production.
- [Wiki Outline](doc/WIKI.md): Recommended structure for a team-facing documentation wiki.

## Core Features

1.  **Branch Protection Enforcement:** Ensures that `stage` and high-level branches (`main` or `release`) have strict pull request reviews, status checks, and access rules (via Organization Rulesets provisioned by `create_org_ruleset.sh`).
2.  **Team Property Synchronization:** Automatically assigns the GitHub Custom Property (`Team`) to repositories based on Markdown access mappings (via `apply_team_properties.py`).

## Prerequisites

1. **GitHub Organization Owner:** You must have owner privileges for the target organization.
2. **Authentication Token:** You must create a Personal Access Token (PAT) with the following scopes:
   - **Classic PAT (Recommended):** `admin:org`, `repo`
   - **Fine-Grained PAT (Org Permissions):** `Administration` (Read/Write), `Custom properties` (Read/Write)
3. **Repository Secret:** Add your PAT as a Repository Secret named `ORG_ADMIN_TOKEN` in the repository running these tools.
4. **Data (Optional):** To map teams and properties to repositories, use the `doc/ONLINESALES_AI_REPO_MAPPING.md` markdown table file.

## Usage

This framework is completely organization-agnostic and relies entirely on GitHub Actions.

1. Navigate to the **Actions** tab in this repository.
2. You will see three distinct operational workflows:
   - **`1. Create Organization Custom Properties`**
   - **`2. Assign Teams to Repositories`**
   - **`3. Enforce Branch Protection Ruleset`**
3. Select the workflow you wish to run, click **Run workflow**, input your Target Organization Name, and execute!
