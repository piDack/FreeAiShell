import sys

import rich
import typer
def config_shell():
    rich.print('''
Hi! 🙌 I am [bold blue]FreeAiShell[/bold blue], [yellow]your powerful terminal assistant[/yellow] 🔥
I am here to assist you with configuring FreeAiShell. 💪
'''[1:])
    typer.confirm('Are you ready to proceed? 🚀', abort=True)

class Config:
    def __init__(self):
        pass
    