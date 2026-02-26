# Planned Parameters, Custom Properties and Team Names

This document outlines the planned structure for parameters, custom properties, and team names to be added and enforced within the GitHub Organization.

## 1. Parameters
Parameters required for GitHub Actions workflows or automation scripts to function correctly.

- **`GH_TOKEN` / `ORG_ADMIN_TOKEN`**: A PAT or App Token with sufficient scopes (`Administration`, `Custom properties`) to manage organization resources.
- **`ORGANIZATION`**: The name of the target GitHub organization.
- **`sync_properties`** *(Boolean)*: Workflow input to trigger the custom property synchronization.
- **`sync_branch_rules`** *(Boolean)*: Workflow input to trigger branch protection rule enforcement.

## 2. Custom Properties
Custom Properties are used to organize repositories and enforce metadata.

- **`Team`** *(String, Required)*: Associates a repository with its primary owning team.
- **`Environment`** *(Single select)*: Specifies the intended deployment environment (e.g., `Development`, `Staging`, `Production`, `Sandbox`).
- **`Compliance_Level`** *(Single select)*: Determines the compliance requirements of a repository (e.g., `High`, `Medium`, `Low`).
- **`Data_Sensitivity`** *(Single select)*: Indicates the classification of data handled by the repository (e.g., `Public`, `Internal`, `Confidential`, `Restricted`).

## 3. Team Names
Proposed standardized names for GitHub Teams to map access and ownership logic effectively.

- **`engineering-core`**: Core platform engineering team.
- **`engineering-frontend`**: Frontend application development team.
- **`engineering-backend`**: Backend services and APIs development team.
- **`data-engineering`**: Data pipeline and warehouse management team.
- **`security-ops`**: Security operations and compliance team.
- **`devops-infra`**: Infrastructure and CI/CD operations team.
- **`qa-automation`**: Quality assurance and automated testing team.
