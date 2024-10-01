#!/bin/bash

# Path to the config file
CONFIG_FILE="$HOME/.nlsconfig.json"

# Check if the config file exists
if [ ! -f "$CONFIG_FILE" ]; then
    echo "Error: Config file not found at $CONFIG_FILE"
    exit 1
fi

# Read API keys from the config file and export them
while IFS="=" read -r key value; do
    # Remove leading/trailing whitespace and quotes
    key=$(echo "$key" | sed 's/^[[:space:]"]*//;s/[[:space:]"]*$//')
    value=$(echo "$value" | sed 's/^[[:space:]"]*//;s/[[:space:]"]*$//')
    
    # Skip null values and non-API_KEYS
    if [ "$value" != "null" ] && [[ $key == *"API_KEY"* ]]; then
        export "$key=$value"
    fi
done < <(jq -r '.API_KEYS | to_entries[] | "\(.key)=\(.value)"' "$CONFIG_FILE")

