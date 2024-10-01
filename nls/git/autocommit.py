import subprocess
import sys
from openai import OpenAI
import os
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn

from nls.prompts import AUTOCOMMIT_ASSISTANT_PROMPT, AUTOCOMMIT_SYSTEM_PROMPT

console = Console()
client = OpenAI()

def get_git_diff():
    try:
        return subprocess.check_output(['git', 'diff', '--staged']).decode('utf-8')
    except subprocess.CalledProcessError:
        console.print("[bold red]Error:[/bold red] Not a git repository or no changes staged.", style="red")
        sys.exit(1)

def generate_commit_message(diff):
    # openai.api_key = os.getenv('OPENAI_API_KEY')
    
    if not os.getenv('OPENAI_API_KEY'):
        console.print("[bold red]Error:[/bold red] OPENAI_API_KEY environment variable not set.", style="red")
        sys.exit(1)

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        progress.add_task(description="Generating commit message...", total=None)
        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": AUTOCOMMIT_SYSTEM_PROMPT},
                    {"role": "user", "content": AUTOCOMMIT_ASSISTANT_PROMPT % diff}
                ]
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            console.print(f"[bold red]Error generating commit message:[/bold red] {str(e)}", style="red")
            sys.exit(1)

def create_commit(message):
    try:
        subprocess.run(['git', 'commit', '-m', message], check=True)
        console.print(Panel.fit(
            f"[bold green]Commit created successfully![/bold green]\n\n"
            f"Message: [cyan]{message}[/cyan]",
            title="Git AutoCommit",
            border_style="green",
        ))
    except subprocess.CalledProcessError:
        console.print("[bold red]Error:[/bold red] Failed to create commit.", style="red")
        sys.exit(1)

def main():
    diff = get_git_diff()
    if not diff:
        console.print("No changes to commit.", style="yellow")
        return

    commit_message = generate_commit_message(diff)
    create_commit(commit_message)

if __name__ == "__main__":
    main()