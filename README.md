# GitHub Governance & Release Workflow Automation

This project contains an enterprise-grade automation suite for enforcing standardized release pipelines and defining repository ownership via GitHub Custom Properties. Built specifically for use and validation within the sandbox organization (**ChinmayDhokTestOrg**), before rolling out to production.

## 🎯 Architecture Overview

1. **Repository Tagging**: Scripts to parse CSV inventory metrics and dynamically assign the GitHub Custom Property (`Team`) to define ownership at the repository level.
2. **Strict Release Pipelines**: Implementation of the `feature -> stage -> release` branching paradigm.
3. **Automated PR Blockers**: A reusable GitHub Action to block any changes targeted to `release` or `main` that did not originate from `stage`.
4. **Enforced Branch Policies**: Python automation to programmatically attach strict branch protection rules using `gh api`.

---

## 🛠 Prerequisites (Org Admin Setup)

Before executing the automation scripts, you need to configure the Test Organization. You can do this by logging into your GitHub App/Admin account.

### 1. Create the `Team` Custom Property
1. Navigate to the [Organization Settings for ChinmayDhokTestOrg](https://github.com/organizations/ChinmayDhokTestOrg/settings/profile).
2. On the left sidebar, under **Code, planning, and automation** (or **Repository**), select **Custom properties**.
3. Click **Add property**.
4. Set the name exactly as: `Team`.
5. Set the property type to **Multi select**.
6. (Optional) Define the list of allowed values. This should correspond to the teams mentioned in your CSV files.
7. Save the custom property.

### 2. Generate a Personal Access Token (PAT)
The scripts require a PAT to communicate with the GitHub API.

1. Go to your personal account settings (Developer Settings -> Personal access tokens -> Fine-grained tokens or Tokens (classic)).
2. Generate a token with the following scopes:
   - `admin:org` (for reading and writing custom properties).
   - `repo` (Full control of private repositories - required for branch protections).
3. Copy the token.
4. Go to the settings of the repository where this automation is stored (within `ChinmayDhokTestOrg`).
5. Under **Security** -> **Secrets and variables** -> **Actions**, click **New repository secret**.
6. Name the secret **`ORG_ADMIN_TOKEN`**.
7. Paste your generated token into the Value box and save.

---

## 📖 Developer Wiki: `feature -> stage -> release` Flow

To maintain absolute stability and a highly audited release pipeline, all developers writing code within this test organization and eventually production must adhere to the Stage-to-Release PR mechanism.

**How to contribute code, step-by-step:**

1. **Branch off `stage` (or `main` if `stage` is identical):**
   ```bash
   git checkout stage
   git checkout -b feature/my-cool-update
   ```
2. **Develop and commit your code.**
3. **Open a Pull Request to `stage`:** Your `feature` branch merges into the `stage` branch first. This requires tests to pass and at least 1 approval (per test org rules).
4. **Deploy and Validate on Stage Environment:** Once merged to `stage`, it should trigger the staging deployments.
5. **Open a Release Pull Request:** When you are ready to prepare a production release, open a Pull Request from `stage` directly into `release` (or `main`).
   > *⚠️ Note: If you attempt to open a Pull Request directly from your `feature` branch into `release`, the `Enforce Release Branch Flow` status check will actively FAIL and prevent you from merging. You cannot bypass this rule.*

---

## 🚀 Deployment Guide

To run the automated GitHub Actions at scale across the organization to sync properties and enforce these rules:

### Preparing the Data
Ensure the following two CSV files exist inside the `.github/scripts/` directory:
1. `github-full-inventory.csv`: Used for identifying all active repositories.
2. `team-access-by-repo.csv`: Used for mapping repositories to teams for Custom Properties. 

*CSV Format Expectations:* Standard headers should be used, typically the repository name column as `repository` or `repo_name` and the team mapping column as `team_name` or `team`.

### Running the Runbook natively (via GitHub Actions)
1. Go to the Actions tab of this repository.
2. Select the **`GitHub Governance Organization Sync`** workflow on the left sidebar.
3. Click the **Run workflow** dropdown on the right side.
4. You will be prompted with two boolean options:
   - **`Sync Custom Properties (Team)`**: Check this to run the Python script mapping the `Team` property to repos based on the CSV data.
   - **`Sync Branch Protection Rules`**: Check this to loop over active repositories and attach branch rules to `stage` and `release`.
5. Click **Run workflow**.

The workflow output will provide verbose logging describing the status of each repository as it interacts with the GitHub API. 
