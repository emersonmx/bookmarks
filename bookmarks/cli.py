import click

from bookmarks import init
from bookmarks.group import cli as group_cli


@click.group()
def cli():
    pass


cli.add_command(init.command)
cli.add_command(group_cli.group)
