# Wiki Outline: Organization Governance 

This document serves as an outline for creating a team-wide Wiki or Knowledge Base article summarizing the new governance enforcement processes.

## Title: GitHub Sandbox Governance & Policy Enforcement

### 1. Introduction
*What is this?*
A brief summary explaining that the organization is enforcing structural integrity and ownership across all 400+ repositories.

### 2. Ownership & Custom Properties
*How do we track ownership?*
- GitHub **Custom Properties** are now the system of record for repository metadata. We rely heavily on the `Team` custom property (a Multi-Select dropdown) to track engineering ownership.
- Property assignments are dictated by centralized mapping documents (`doc/ONLINESALES_AI_REPO_MAPPING.md`).
- Developers and managers can view a repository's ascribed properties in the repository's Settings or on the organization's Repository overview page.

### 3. Branching Strategy & Restrictions
*What rules are enforced?*
- **The `stage` branch:** Explain that this branch is the testing ground. Describe the strict protections applied (Required PRs, 2 Approvals, CI checks).
- **The `release`/`main` branches:** Explain that these are production branches. Describe the strict protections (Required PRs, 2 Approvals, CI check tied to a required origin branch: `Verify Source Branch is Stage`).

### 4. Workflows & Automation
*How is it applied?*
- The entire enforcement mechanism is Organization-Agnostic and runs entirely in the cloud via GitHub Actions.
- An Organization Owner navigates to the **Actions** tab to run any of the three decoupled management workflows:
- **`1. Create Organization Custom Properties`:** Builds out the `Team` Custom Property schema and populates the dropdown with all distinct teams.
- **`2. Assign Teams to Repositories`:** Iterates through the Markdown mapping table to automatically assign the correct teams to the `Team` metadata on each repository.
- **`3. Enforce Branch Protection Ruleset`:** Provisions a massive `Enforce Standard Branch Flows` Organization Ruleset that locks down branch protections across all repositories at once.

### 5. FAQ / Troubleshooting
### 5. FAQ / Troubleshooting
*What if I am blocked?*

**Q: My repository isn't in the mapping CSV. Does it still get protected?**
Yes. The branch protections are applied across the entire organization (all repositories) via a fundamental Organization Ruleset. Even if your repo isn't assigned a specific `Team` property, it is still protected.

**Q: I need to override branch protections in an emergency. Who do I contact?**
Reach out to the Organization Admins. Due to the "Bypass Actors" rule we configured, only users with `OrganizationAdmin` privileges can bypass the branch protections.

**Q: How do we update a repository's team mapping?**
Update the internal mapping tracking document (`doc/ONLINESALES_AI_REPO_MAPPING.md`). Once approved, an Admin will trigger the `2. Assign Teams to Repositories` GitHub Action workflow to push the changes natively to the repository UI.
