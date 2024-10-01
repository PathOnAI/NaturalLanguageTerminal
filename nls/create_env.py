import os
import sys
import typer
import json
from rich.console import Console

from nls.core.system import SystemInfo

console = Console()

def create_nls_environment(env_name):
    if os.path.exists(env_name):
        console.print(f"[bold red]Error:[/bold red] Directory '{env_name}' already exists", style="red")
        raise typer.Exit(code=1)

    os.makedirs(os.path.join(env_name, 'bin'))
    os.makedirs(os.path.join(env_name, 'static'))

    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    if sys.platform == "win32":
        scripts = [
            ('activate_template.bat', 'activate.bat'),
            ('end_template.bat', 'nls_end.bat'),
            # ('nls_interceptor.bat', 'nls_interceptor.bat')
        ]
    else:
        scripts = [
            ('activate_template.sh', 'activate'),
            ('end_template.sh', 'nls_end'),
            ('interceptor.sh', 'interceptor.sh')
        ]

    for template, new_name in scripts:
        try:
            with open(os.path.join(script_dir, 'shell_scripts', template), 'r', encoding='utf-8') as f:
                content = f.read()
        except UnicodeDecodeError:
            # If UTF-8 fails, try with 'utf-8-sig' to handle BOM
            with open(os.path.join(script_dir, 'shell_scripts', template), 'r', encoding='utf-8-sig') as f:
                content = f.read()
        
        content = content.replace('{{ENV_NAME}}', env_name)

        with open(os.path.join(env_name, 'bin', new_name), 'w', encoding='utf-8') as f:
            f.write(content)
        
        # Make scripts executable (no effect on Windows)
        os.chmod(os.path.join(env_name, 'bin', new_name), 0o755)

    system_info = SystemInfo()

    with open(os.path.join(env_name, 'static', 'os_info.json'), 'w', encoding='utf-8') as f:
        f.write(json.dumps(system_info.get_all_info()))

    console.print(f"[green]NLS environment '{env_name}' created successfully.[/green]")
    
    if sys.platform == "win32":
        console.print(f"[yellow]To activate, run: {env_name}\\bin\\activate.bat[/yellow]")
    else:
        console.print(f"[yellow]To activate, run: source {env_name}/bin/activate[/yellow]")

if __name__ == "__main__":
    typer.run(create_nls_environment)