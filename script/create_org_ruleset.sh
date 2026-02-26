#!/bin/bash

# ==============================================================================
# GitHub Organization Ruleset Creator via GitHub CLI
# ==============================================================================
# This script creates an Organization-level Repository Ruleset to enforce
# branch protection rules across the target organization without needing
# to apply protections repository-by-repository.
# 
# PREREQUISITES:
# - You must be authenticated to `gh` with the `admin:org` scope:
#   `gh auth refresh -h github.com -s admin:org`
# - You must be an Organization Owner.
# ==============================================================================

ORG_NAME=${ORGANIZATION}

if [ -z "$ORG_NAME" ]; then
  echo "Error: ORGANIZATION environment variable is required."
  exit 1
fi
RULESET_NAME="Enforce Standard Branch Flows"

echo "Creating Organization Ruleset ('$RULESET_NAME') for: $ORG_NAME"

# The Ruleset JSON Payload
# Enforces Required PRs and 2 Approvals on stage, release, main, and master branches.
cat << 'EOF' > ruleset_payload.json
{
  "name": "Enforce Standard Branch Flows",
  "target": "branch",
  "enforcement": "active",
  "bypass_actors": [
    {
      "actor_id": 1,
      "actor_type": "OrganizationAdmin",
      "bypass_mode": "always"
    }
  ],
  "conditions": {
    "ref_name": {
      "exclude": [],
      "include": [
        "refs/heads/stage",
        "refs/heads/release",
        "refs/heads/main",
        "refs/heads/master"
      ]
    },
    "repository_name": {
      "exclude": [],
      "include": [
        "~ALL"
      ]
    }
  },
  "rules": [
    {
      "type": "pull_request",
      "parameters": {
        "required_approving_review_count": 2,
        "dismiss_stale_reviews_on_push": true,
        "require_code_owner_review": false,
        "require_last_push_approval": false,
        "required_review_thread_resolution": false
      }
    },
    {
      "type": "required_status_checks",
      "parameters": {
        "strict_required_status_checks_policy": true,
        "required_status_checks": [
          {
            "context": "Verify Source Branch is Stage"
          }
        ]
      }
    },
    {
      "type": "deletion"
    },
    {
      "type": "non_fast_forward"
    }
  ]
}
EOF

# Make the API call using gh
gh api \
  --method POST \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  /orgs/$ORG_NAME/rulesets \
  --input ruleset_payload.json

# Cleanup
rm ruleset_payload.json

echo ""
echo "Organization ruleset creation attempted."
