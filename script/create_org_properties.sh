#!/bin/bash

# ==============================================================================
# GitHub Organization Custom Property Schema Creator
# ==============================================================================
# Triggers via `gh` CLI in a GitHub Action to ensure the required Custom Properties
# exist at the organization level before they are assigned to repositories.

ORG_NAME=${ORGANIZATION:-"ChinmayDhokTestOrg"}

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

# 1. Team (String)
cat << 'EOF' > prop_payload.json
{
  "value_type": "string",
  "required": false,
  "description": "The logical engineering team responsible for this repository."
}
EOF
create_property "Team" "prop_payload.json"

# 2. BU (String)
cat << 'EOF' > prop_payload.json
{
  "value_type": "string",
  "required": false,
  "description": "The Business Unit that this repository falls under."
}
EOF
create_property "BU" "prop_payload.json"

# 3. Environment (Single Select)
cat << 'EOF' > prop_payload.json
{
  "value_type": "single_select",
  "required": false,
  "description": "The intended runtime environment.",
  "allowed_values": ["Development", "Staging", "Production", "Sandbox", "DR"]
}
EOF
create_property "Environment" "prop_payload.json"

# 4. Compliance_Level (Single Select)
cat << 'EOF' > prop_payload.json
{
  "value_type": "single_select",
  "required": false,
  "description": "The compliance level required for this repository.",
  "allowed_values": ["High", "Medium", "Low", "None"]
}
EOF
create_property "Compliance_Level" "prop_payload.json"

# 5. Data_Sensitivity (Single Select)
cat << 'EOF' > prop_payload.json
{
  "value_type": "single_select",
  "required": false,
  "description": "Classification of data handled by this repository.",
  "allowed_values": ["Public", "Internal", "Confidential", "Restricted"]
}
EOF
create_property "Data_Sensitivity" "prop_payload.json"


rm prop_payload.json
echo "Schema definition complete."
