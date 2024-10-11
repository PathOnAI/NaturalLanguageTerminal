import typer
import time
import os
import json
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.prompt import Prompt
from ..create_env import create_nlt_environment

app = typer.Typer()
console = Console()

CONFIG_FILE = os.path.expanduser("~/.nltconfig.json")

def check_init():
    return os.path.exists(CONFIG_FILE)

@app.command()
def init():
    """Initialize nlt configuration interactively."""
    if check_init():
        console.print("[yellow]Config file already exists. Overwriting...[/yellow]")
    
    config = {
        "API_KEYS": {
            "OPENAI_API_KEY": None,
            # "GROQ_API_KEY": None
        },
        "LLM_OPTIONS": ["gpt-4", "gpt-3.5-turbo", "gpt-4-turbo-preview"],
        "CURRENT_LLM": None
    }
    
    console.print("[bold]Welcome to nlt Configuration![/bold]")
    
    for api in config["API_KEYS"]:
        value = Prompt.ask(f"Enter your {api} API key", default="")
        config["API_KEYS"][api] = value if value else None
    
    current_llm = Prompt.ask("Choose your default LLM", choices=config["LLM_OPTIONS"], default=config["LLM_OPTIONS"][0])
    config["CURRENT_LLM"] = current_llm
    
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=2)
    
    console.print(Panel.fit(
        "[bold green]nlt configuration initialized![/bold green]\n\n"
        f"Config file created at: [cyan]{CONFIG_FILE}[/cyan]\n"
        "You can edit this file manually later if needed.",
        title="nlt Initialization",
        border_style="green",
    ))

@app.command()
def create(env_name: str):
    """Create a new nlt environment."""
    if not check_init():
        console.print("[bold red]Error: nlt is not initialized.[/bold red]")
        console.print("Please run [cyan]@nlt init[/cyan] first to set up your configuration.")
        return

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        task = progress.add_task(description="Creating nlt environment...", total=None)
        status = create_nlt_environment(env_name)
        progress.update(task, completed=100)
        time.sleep(0.5)  # Allow a moment for the spinner to complete visually
        # return
    
    if status == 0:
        # console.print(f"[green]nlt environment '{env_name}' created successfully.[/green]")
        console.print(f"\n")
    elif status == 1:
        console.print(f"[bold red]Error:[/bold red] Directory '{env_name}' already exists", style="red")
    


    console.print(Panel.fit(
        f"[bold green]nlt environment '{env_name}' created successfully![/bold green]\n\n"
        f"To activate, run:\n"
        f"[cyan]source {env_name}/bin/activate[/cyan]\n\n"
        f"To deactivate, run:\n"
        f"[cyan]deactivate[/cyan]\n",
        title="nlt Environment Created",
        border_style="green",
    ))

@app.command()
def config():
    """View or edit the current configuration."""
    if not check_init():
        console.print("[bold red]Error: nlt is not initialized.[/bold red]")
        console.print("Please run [cyan]@nlt init[/cyan] first to set up your configuration.")
        return

    with open(CONFIG_FILE, 'r') as f:
        config = json.load(f)
    
    console.print("[bold]Current Configuration:[/bold]")
    console.print(json.dumps(config, indent=2))
    
    if Prompt.ask("Do you want to edit the configuration?", choices=["y", "n"], default="n") == "y":
        for api in config["API_KEYS"]:
            value = Prompt.ask(f"Enter your {api} API key", default=config["API_KEYS"][api] or "")
            config["API_KEYS"][api] = value if value else None
        
        current_llm = Prompt.ask("Choose your default LLM", choices=config["LLM_OPTIONS"], default=config["CURRENT_LLM"])
        config["CURRENT_LLM"] = current_llm
        
        with open(CONFIG_FILE, 'w') as f:
            json.dump(config, f, indent=2)
        
        console.print("[green]Configuration updated successfully.[/green]")
    else:
        console.print("Configuration not changed.")