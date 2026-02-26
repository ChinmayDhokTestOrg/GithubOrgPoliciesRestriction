#!/bin/bash

# ==============================================================================
# GitHub Organization Custom Property Schema Creator
# ==============================================================================
# Triggers via `gh` CLI in a GitHub Action to ensure the required Custom Properties
# exist at the organization level before they are assigned to repositories.

ORG_NAME=${ORGANIZATION}

if [ -z "$ORG_NAME" ]; then
  echo "Error: ORGANIZATION environment variable is required."
  exit 1
fi

echo "Creating/Updating Custom Property Schemas for: $ORG_NAME..."

# Helper function to create/update a property
create_property() {
  local prop_name=$1
  local payload_file=$2
  
  echo " > Processing property: '$prop_name'..."
  
  gh api \
    --method PUT \
    -H "Accept: application/vnd.github+json" \
    -H "X-GitHub-Api-Version: 2022-11-28" \
    /orgs/$ORG_NAME/properties/schema/$prop_name \
    --input $payload_file > /dev/null 2>&1
    
   if [ $? -eq 0 ]; then
     echo "   [SUCCESS] $prop_name schema defined."
   else
     echo "   [WARN/ERROR] Could not apply $prop_name. Ensure the token has sufficient admin:org privileges."
   fi
}

# Note: The Team schema is now created dynamically by apply_team_properties.py
# because it parses the allowed values directly from the ONLINESALES_AI_REPO_MAPPING.md file.

rm prop_payload.json
echo "Schema definition complete."
