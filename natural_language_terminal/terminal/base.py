import sys
import json
import os
import requests

from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich.text import Text

from natural_language_terminal.prompts import TERMINAL_COMMAND_ASSISTANT_PROMPT
from natural_language_terminal.terminal.utils import parse_ai_response_for_bash_and_zsh

from dotenv import load_dotenv

load_dotenv()

console = Console()

def format_response(content: str) -> Panel:
    title = Text("nlt Suggestion", style="bold magenta")
    syntax = Syntax(content, "markdown", theme="monokai", line_numbers=True)
    return Panel(syntax, title=title, expand=False, border_style="green")

def make_prompt(cmd: str):
    print(cmd)
    return TERMINAL_COMMAND_ASSISTANT_PROMPT % cmd

def make_api_request(cmd: str, api_url: str, api_key: str) -> dict:
    prompt = make_prompt(cmd)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    data = {
        "model": "gpt-4o",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }
    
    with console.status("Thinking...", spinner="dots"):
        response = requests.post(api_url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()

def write_to_file(user_choice: str, generated_command: str):
    with open("execution_permissions.log", "w") as f:
        f.write(f"{user_choice}\n{parse_ai_response_for_bash_and_zsh(generated_command)}")

def main(command: str):
    api_url = 'https://api.openai.com/v1/chat/completions'
    api_key = os.getenv('OPENAI_API_KEY')

    if not api_url or not api_key:
        console.print("[bold red]Error:[/bold red] API_URL and API_KEY must be set as environment variables")
        sys.exit(1)

    try:
        response = make_api_request(command, api_url, api_key)
        content = response['choices'][0]['message']['content']
        
        formatted_response = format_response(content)
        console.print(formatted_response)

        user_choice = console.input("Do you want to run this command? (y/n): ").lower()
        write_to_file(user_choice, content)

    except requests.RequestException as e:
        console.print(f"[bold red]Error making API request:[/bold red] {str(e)}")
        sys.exit(1)
    except (KeyError, IndexError) as e:
        console.print(f"[bold red]Error parsing API response:[/bold red] {str(e)}")
        console.print(Panel(json.dumps(response, indent=2), title="Raw Response", border_style="red"))
        sys.exit(1)
    except Exception as e:
        console.print(f"[bold red]An unexpected error occurred:[/bold red] {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()