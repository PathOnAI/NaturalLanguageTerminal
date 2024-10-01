#!/bin/bash

# Unset the git alias
git config --global --unset alias.autocommit

# Restore the old PATH and PS1
export PATH="$OLD_PATH"
export PS1="$OLD_PS1"

#end interceptor
eval "intercept"

# Unset NLS-specific environment variables
unset NLS_ACTIVE
unset NLS_PYTHON_PATH
unset OLD_PATH
unset OLD_PS1

# ANSI color codes
RED='\033[0;31m'
NC='\033[0m' # No Color

# Print stylized deactivation message
echo -e "\n${RED}┌────────────────────────────────────────────┐${NC}"
echo -e "${RED}│${NC}                                            ${RED}│${NC}"
echo -e "${RED}│${NC}   NLS environment deactivated successfully ${RED}│${NC}"
echo -e "${RED}│${NC}                                            ${RED}│${NC}"
echo -e "${RED}└────────────────────────────────────────────┘${NC}\n"

# Default values
cleanup=false
additional_param=""

# Parse command line arguments
while [[ "$#" -gt 0 ]]; do
    case $1 in
        -c|--cleanup) cleanup=true ;;
        *) echo "Unknown parameter: $1. Must be either -c or --cleanup"; exit 1 ;;
    esac
    shift
done


# Check if cleanup flag is set
if [ "$cleanup" = true ] ; then
    FILE_DIR=$(dirname "$(dirname "$(readlink -f "$0")")")

    # Print stylized deactivation message
    echo -e "\n${RED}┌────────────────────────────────────────────┐${NC}"
    echo -e "${RED}│${NC}                                            ${RED}│${NC}"
    echo -e "${RED}│${NC}   NLS Environment Cleaned Up Successfully  ${RED}│${NC}"
    echo -e "${RED}│${NC}                                            ${RED}│${NC}"
    echo -e "${RED}└────────────────────────────────────────────┘${NC}\n"

    # eval "rm -rf \"$FILE_DIR\" && rmdir \"$FILE_DIR\""
    eval "rm -rf \"$FILE_DIR\""
fi

# Unset the function itself
# unset -f nls_end