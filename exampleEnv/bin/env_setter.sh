#!/bin/bash

# Path to the config file
CONFIG_FILE="$HOME/.nltconfig.json"

# Check if the config file exists
if [ ! -f "$CONFIG_FILE" ]; then
    echo "Error: Config file not found at $CONFIG_FILE"
    exit 1
fi

# Check if jq is installed
if ! command -v jq &> /dev/null; then
    echo "Error: jq is not installed. Please install it first."
    exit 1
fi

# Read API keys from the config file and export them
jq -r '.API_KEYS | to_entries[] | "\(.key)=\(.value)"' "$CONFIG_FILE" | while IFS= read -r line; do
    # Skip empty lines
    [ -z "$line" ] && continue
    
    # Split the line into key and value
    key="${line%%=*}"
    value="${line#*=}"
    
    # Skip null values and only process API_KEY entries
    if [ "$value" != "null" ] && [[ $key == *"API_KEY"* ]]; then
        # Remove any surrounding quotes from the value
        value="${value%\"}"
        value="${value#\"}"
        
        # Export the environment variable
        export "$key=$value"
        echo "Exported: $key"
    fi
done

