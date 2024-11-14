import os
import typer
import json
from rich.console import Console
from natural_language_terminal.core.system import SystemInfo

console = Console()

def create_nlt_environment(env_name):
    if os.path.exists(env_name):
        return 1

    os.makedirs(os.path.join(env_name, 'bin'))
    os.makedirs(os.path.join(env_name, 'static'))

    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # MacOS-specific scripts
    scripts = [
        ('activate_template.sh', 'activate'),
        ('end_template.sh', 'nlt_end'),
        ('interceptor.sh', 'interceptor.sh'),
        ('env_setter.sh', 'env_setter.sh')
    ]

    for template, new_name in scripts:
        template_path = os.path.join(script_dir, 'shell_scripts', template)
        output_path = os.path.join(env_name, 'bin', new_name)
        
        # Read with Unix line endings
        with open(template_path, 'r', encoding='utf-8', newline='\n') as f:
            content = f.read()
        
        # Replace environment name
        content = content.replace('{{ENV_NAME}}', env_name)
        
        # Write with Unix line endings
        with open(output_path, 'w', encoding='utf-8', newline='\n') as f:
            f.write(content)
        
        # Make scripts executable
        os.chmod(output_path, 0o755)

    # Write system info
    system_info = SystemInfo()
    with open(os.path.join(env_name, 'static', 'os_info.json'), 'w', encoding='utf-8') as f:
        f.write(json.dumps(system_info.get_all_info()))

    return 0

if __name__ == "__main__":
    typer.run(create_nlt_environment)