#!/bin/bash
# This script works for both Bash and Zsh

# Variable to store intercepted commands
INTERCEPTED_COMMAND=""

# Variable to control interception state
INTERCEPTION_ACTIVE=false

# Function to log the command
log_command() {
    local cmd="$1"
    echo "Command intercepted: $cmd" >> ~/.intercepted_commands.log
}

# Function to be used as a trap
intercept_command() {
    if $INTERCEPTION_ACTIVE; then
        # Get the command that's about to be executed
        local cmd="$BASH_COMMAND"

        if [[ -n "$ZSH_VERSION" ]]; then
            cmd="$1"
            # trap - DEBUG
        fi
        
        # Ignore specific commands
        case "$cmd" in
            intercept|last_intercepted|toggle_interception|show_last_intercepted)
                return 0
                ;;
        esac
        
        # Store and log the command
        INTERCEPTED_COMMAND="$cmd"
        log_command "$INTERCEPTED_COMMAND"
        
        # Prevent the command from executing
        if [[ -n "$ZSH_VERSION" ]]; then
            return 1
        else
            kill -INT $$
        fi
    fi
}

# Function to toggle command interception
toggle_interception() {
    if $INTERCEPTION_ACTIVE; then
        INTERCEPTION_ACTIVE=false
        if [[ -n "$ZSH_VERSION" ]]; then
            if (( ${#preexec_functions[@]} )); then
                preexec_functions=("${preexec_functions[@]:#intercept_command}")
            fi
        else
            trap - DEBUG
        fi
    else
        INTERCEPTION_ACTIVE=true
        if [[ -n "$ZSH_VERSION" ]]; then
            if ! (( ${preexec_functions[(Ie)intercept_command]} )); then
                preexec_functions+=(intercept_command)
            fi
        else
            trap 'intercept_command' DEBUG
        fi
    fi
}

# Alias to easily toggle interception
alias intercept='toggle_interception'

# Function to show the last intercepted command
show_last_intercepted() {
    if [[ -n "$INTERCEPTED_COMMAND" ]]; then
        echo "Last intercepted command: $INTERCEPTED_COMMAND"
    else
        echo "No command has been intercepted yet."
    fi
}

# Alias to show last intercepted command
alias last_intercepted='show_last_intercepted'

# zsh specific handler 
command_not_found_handler() {
    if $INTERCEPTION_ACTIVE; then
        ai_message_generator "$*"
    else
        echo "zsh: command not found: $*"
    fi
}

ai_message_generator() {
    local cmd="$*"
   
    eval "$nlt_PYTHON_PATH -c \"from nlt.terminal.base import main; main('$cmd')\""

    if [ $? -ne 0 ]; then
        echo "Error occurred while processing the API response."
        return 1
    fi

    filename="execution_permissions.log"

    # Check if the file exists
    if [ ! -f "$filename" ]; then
        echo "Error: File '$filename' not found"
        exit 1
    fi

    # Read the first two lines from the file
    read -r line1 < "$filename"
    read -r line2 < <(sed -n '2p' "$filename")

    # Convert line1 to lowercase for case-insensitive comparison
    line1_lower=$(echo "$line1" | tr '[:upper:]' '[:lower:]')

    # Check if the first line is 'y'
    if [ "$line1_lower" = "y" ]; then
        eval "$line2"
    else
        echo "No command executed"
    fi

    return 0
}
