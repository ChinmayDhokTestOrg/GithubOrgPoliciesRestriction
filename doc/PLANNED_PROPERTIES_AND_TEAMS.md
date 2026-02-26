# Planned Parameters, Custom Properties and Team Names

This document outlines the planned structure for parameters, custom properties, and team names to be configured at the Organization level natively via the GitHub API.

## 1. Parameters (Workflow Secrets)
Parameters required for GitHub Actions workflows or automation scripts to function properly.

- **`ORG_ADMIN_TOKEN`**: A PAT or App Token with sufficient scopes (`admin:org`, `Custom properties: read/write`) stored as a repository secret.
- **`ORGANIZATION`**: The name of the target GitHub organization, configured as an environment variable in the workflow.

## 2. Organization Custom Properties
Custom Properties are used to organize repositories and enforce metadata systematically. These are managed centrally at the Org level.

- **`Team`** *(String, Optional)*: Associates a repository with its primary owning logical team.
- **`BU`** *(String, Optional)*: The Business Unit that this repository belongs to.
- **`Environment`** *(Single select: `Development`, `Staging`, `Production`, `Sandbox`, `DR`)*: Specifies the intended deployment environment.
- **`Compliance_Level`** *(Single select: `High`, `Medium`, `Low`, `None`)*: Determines the compliance requirements of a repository.
- **`Data_Sensitivity`** *(Single select: `Public`, `Internal`, `Confidential`, `Restricted`)*: Indicates the classification of data handled by the repository.

## 3. Team Names
Proposed standardized names for GitHub Teams to map access and ownership logic effectively.

- **`engineering-core`**: Core platform engineering team.
- **`engineering-frontend`**: Frontend application development team.
- **`engineering-backend`**: Backend services and APIs development team.
- **`data-engineering`**: Data pipeline and warehouse management team.
- **`security-ops`**: Security operations and compliance team.
- **`devops-infra`**: Infrastructure and CI/CD operations team.
- **`qa-automation`**: Quality assurance and automated testing team.
