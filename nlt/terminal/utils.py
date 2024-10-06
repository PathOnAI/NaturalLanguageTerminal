def parse_ai_response_for_bash_and_zsh(ai_response: str):
    # Remove any leading/trailing whitespace
    ai_response = ai_response.strip()
    
    # Split the response into lines
    lines = ai_response.split('\n')
    
    parsed_commands = []
    current_command = ""
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Check if the line ends with a backslash (line continuation)
        if line.endswith('\\'):
            current_command += line[:-1] + " "
        else:
            current_command += line
            parsed_commands.append(current_command.strip())
            current_command = ""
    
    # If there's any remaining command (in case the last line had a backslash)
    if current_command:
        parsed_commands.append(current_command.strip())
    
    # Join commands with semicolons for bash execution
    bash_ready_command = '; '.join(parsed_commands)
    
    # Escape single quotes
    bash_ready_command = bash_ready_command.replace("'", "'\\''")
    
    return bash_ready_command
