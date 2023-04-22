import os
import time
from rich.console import Console
import typer
from typer import Typer
from config import Config
from backend_factory import QueryClientFactory

cli_app = Typer()

@cli_app.command()
def aishell(question: str):
    config = Config.load()
    backend=config.backend
    query_client=QueryClientFactory(backend)
    console = Console()
    with console.status(f'''
[green] AiShell is thinking of `{question}` ...[/green]

[dim]AiShell is not responsible for any damage caused by the command executed by the user.[/dim]'''[1:]):
        start_time = time.time()
        response = query_client.query(construct_prompt(question))
        end_time = time.time()

    execution_time = end_time - start_time
    console.print(f'AiShell: {response}\n\n[dim]Took {execution_time:.2f} seconds to think the command.[/dim]')
    will_execute = typer.confirm('Execute this command?')
    if will_execute:
        os.system(response)

@cli_app.command()
def ais_connect_test():
    pass

import os
def construct_prompt(query: str) -> str:
    return f'''
Translate the following task to a {os.uname()[0]} shell command. Users provide a text-query as input.
Provide ONLY the command in ONE LINE, with no explanation:

One-line command for: {query}
'''[1:]