# Wiki Outline: Organization Governance 

This document serves as an outline for creating a team-wide Wiki or Knowledge Base article summarizing the new governance enforcement processes.

## Title: GitHub Sandbox Governance & Policy Enforcement

### 1. Introduction
*What is this?*
A brief summary explaining that the organization is enforcing structural integrity and ownership across all 400+ repositories.

### 2. Ownership & Custom Properties
*How do we track ownership?*
- GitHub **Custom Properties** are now the system of record for repository metadata. This includes properties like `Team`, `BU`, `Environment`, `Compliance_Level`, and `Data_Sensitivity`.
- Property assignments are dictated by centralized mapping documents (e.g., `doc/ONLINESALES_AI_REPO_MAPPING.md`).
- Developers and managers can view a repository's ascribed properties in the repository's Settings or on the organization's Repository overview page.

### 3. Branching Strategy & Restrictions
*What rules are enforced?*
- **The `stage` branch:** Explain that this branch is the testing ground. Describe the strict protections applied (Required PRs, 2 Approvals, CI checks).
- **The `release`/`main` branches:** Explain that these are production branches. Describe the strict protections (Required PRs, 2 Approvals, CI check tied to a required origin branch: `Verify Source Branch is Stage`).

### 4. Workflows & Automation
*How is it applied?*
- The entire enforcement mechanism is Organization-Agnostic and runs entirely in the cloud.
- An Organization Owner navigates to the `GitHub Governance Organization Sync` workflow in the **Actions** tab.
- They input the target organization's name into the workflow parameters and execute it.
- **Phase 1:** The action builds out all Custom Property schemas required by the organization.
- **Phase 2:** The action iterates through uploaded CSVs to automatically assign teams and roles to the `Team` custom property.
- **Phase 3:** The action provisions a massive `Enforce Standard Branch Flows` Organization Ruleset that locks down branch protections across all repositories at once.

### 5. FAQ / Troubleshooting
### 5. FAQ / Troubleshooting
*What if I am blocked?*

**Q: My repository isn't in the mapping CSV. Does it still get protected?**
Yes. The branch protections are applied across the entire organization (all repositories) via a fundamental Organization Ruleset. Even if your repo isn't assigned a specific `Team` property, it is still protected.

**Q: I need to override branch protections in an emergency. Who do I contact?**
Reach out to the Organization Admins. Due to the "Bypass Actors" rule we configured, only users with `OrganizationAdmin` privileges can bypass the branch protections.

**Q: How do we update a repository's team mapping?**
Update the internal mapping tracking document (e.g., `doc/ONLINESALES_AI_REPO_MAPPING.md`). Once approved by management, convert it to a CSV and an Admin will trigger the *GitHub Governance Organization Sync* workflow to push the changes.
