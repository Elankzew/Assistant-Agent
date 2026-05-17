"""Command-line interface for Assistant Agent."""

from __future__ import annotations

import click
from rich.console import Console

from assistant_agent import __version__
from assistant_agent.agent import Agent

console = Console()


@click.group()
@click.version_option(__version__, prog_name="assistant-agent")
def main() -> None:
    """Assistant Agent CLI."""


@main.command()
@click.argument("message")
@click.option("--name", default="Assistant", help="Agent display name.")
def chat(message: str, name: str) -> None:
    """Send a single message to the agent and print the response."""
    agent = Agent(name=name)
    reply = agent.respond(message)
    console.print(f"[bold cyan]{name}[/bold cyan]: {reply}")


@main.command()
def info() -> None:
    """Show package info."""
    console.print(f"[bold]assistant-agent[/bold] version [green]{__version__}[/green]")


if __name__ == "__main__":
    main()
