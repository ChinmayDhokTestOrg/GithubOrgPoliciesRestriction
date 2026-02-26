# GitHub Organization UI Configuration Guide

This guide provides step-by-step instructions for organization administrators to manually configure Custom Properties, assign them to repositories, and set up Organization-Level Branch Protection Rulesets entirely through the GitHub Web UI.

## Part 1: Managing Custom Properties

Custom properties act as powerful metadata assigned to repositories (e.g., `Team`).

### A. Creating the `Team` Custom Property
1. Navigate to your **Organization Profile** on GitHub.
2. Click on the **Settings** tab (the gear icon, usually at the top right).
3. In the left-hand sidebar, scroll down to the **Repository** section and click on **Custom properties**.
4. Click the green **New property** button.
5. **Property Details:**
   - **Name:** Enter `Team`
   - **Type:** Select `Multi Select`
   - **Description:** Enter "The engineering teams responsible for this repository."
   - **Allowed values:** Type in each team name (e.g., `ui`, `infra`, `data`) and press Enter after each to add them to the dropdown list.
   - **Required:** Check this box ONLY if you want to block creation of new repositories that don't have a team assigned.
6. Click **Save property**.

### B. Assigning Teams to Repositories
1. Still in the **Organization Settings -> Repository -> Custom properties** view, switch from the "Properties" tab to the **Set values** tab.
2. You will see a list of all repositories in the organization.
3. Use the **Search repositories** bar to find a specific repository.
4. Check the box to the left of the repository name (or select multiple checkboxes to bulk-assign properties).
5. Click on the **Edit property values** button that appears.
6. In the modal, locate the `Team` property, and select the appropriate team(s) from the dropdown.
7. Click **Save** to apply the ownership metadata.

---

## Part 2: Enforcing Branch Protections (Organization Rulesets)

*Note: Organization-level rulesets require the **GitHub Team** or **GitHub Enterprise** subscription plan.*

### A. Creating the "Enforce Standard Branch Flows" Ruleset
1. Navigate to your **Organization Settings**.
2. In the left-hand sidebar, under the **Repository** section, click on **Rulesets**.
3. Click the green **New branch ruleset** button.
4. **General Configuration:**
   - **Name:** Enter `Enforce Standard Branch Flows`
   - **Enforcement status:** Select `Active`
5. **Bypass List:**
   - Click **Add bypass**. Search for the `OrganizationAdmin` role.
   - Set the bypass capability to `Always` (this allows Admins to override the rule in an emergency).
6. **Target Repositories:**
   - Click **Add target**. Choose `All repositories` to blanket protect the entire organization.
7. **Target Branches:**
   - Click **Add target**. Choose `Include by pattern`.
   - Enter `stage`, click Add.
   - Enter `release`, click Add.
   - Enter `main`, click Add.
   - Enter `master`, click Add.

### B. Configuring the Specific Protection Rules
Scroll down to the **Branch rules** section within the ruleset configuration and check the following boxes:

1. **[x] Restrict deletions:** Prevents anyone from deleting these critical branches.
2. **[x] Require a pull request before merging:**
   - Set **Required approvals** to `2`.
   - Check `Dismiss stale pull request approvals when new commits are pushed` (Optional but highly recommended).
3. **[x] Require status checks to pass:**
   - Click inside the "Search and add status checks" search box.
   - Type in the exact name of the workflow job that controls the pipeline flow: `Verify Source Branch is Stage` and select it.
   - *(Note: This GitHub Action workflow must be present in the repositories for this check to run and pass).*
4. **[x] Block force pushes:** Prevents anyone from rewriting the commit history of these critical branches.

Click the green **Create** button at the very bottom. The organization is now protected natively!
