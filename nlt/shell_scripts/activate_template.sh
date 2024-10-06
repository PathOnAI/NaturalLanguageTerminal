#!/bin/bash

# Get the directory of the current script
FILE_DIR=$(dirname "$(readlink -f "$0")")

# Save the current PATH and PS1
export OLD_PATH="$PATH"
export OLD_PS1="$PS1"

# Add the script directory to PATH
export PATH="$FILE_DIR:$PATH"

# Save the current Python interpreter path
if command -v python &> /dev/null; then
    export nlt_PYTHON_PATH=$(which python)
elif command -v python3 &> /dev/null; then
    export nlt_PYTHON_PATH=$(which python3)
else
    echo "Error: Neither python nor python3 found in PATH"
    exit 1
fi

# Create the git-autocommit alias using the full path to Python
git config --global alias.autocommit "!$nlt_PYTHON_PATH -c \"from nlt.git.autocommit import main; main()\""

alias remove="source $FILE_DIR/nlt_end"

source "$FILE_DIR/interceptor.sh"

eval "intercept"

# Set a flag to indicate nlt is active
export nlt_ACTIVE=1

source "$FILE_DIR/env_setter.sh"

if [ -n "$BASH_VERSION" ]; then
    # Navy blue color code for Bash
    navy_blue="\[\e[38;5;17m\]"
    reset_color="\[\e[0m\]"
    
    # Modify PS1 for Bash
    export PS1="${navy_blue}[nlt~{{ENV_NAME}}]${reset_color} $PS1"
elif [ -n "$ZSH_VERSION" ]; then
    # Navy blue color code for Zsh
    navy_blue="%F{17}"
    reset_color="%f"
    
    # Modify PROMPT for Zsh
    export PROMPT="${navy_blue}[nlt~{{ENV_NAME}}]${reset_color} $PROMPT"
fi

# ANSI color codes
GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Print stylized activation message
echo -e "\n${GREEN}┌────────────────────────────────────────────┐${NC}"
echo -e "${GREEN}│                                            │${NC}"
echo -e "${GREEN}│   ${YELLOW}nlt environment activated successfully${NC}   ${GREEN}│${NC}"
echo -e "${GREEN}│                                            │${NC}"
echo -e "${GREEN}├────────────────────────────────────────────┤${NC}"
echo -e "${GREEN}│                                            │${NC}"
echo -e "${GREEN}│${NC}   Environment: ${CYAN}{{ENV_NAME}}${NC}                     ${GREEN}│${NC}"
echo -e "${GREEN}│   ${NC}To end the session, type: ${CYAN}remove${NC}       ${GREEN}│${NC}"
echo -e "${GREEN}│                                            │${NC}"
echo -e "${GREEN}└────────────────────────────────────────────┘${NC}\n"

