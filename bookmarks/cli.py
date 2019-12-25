import click

from bookmarks import init
from bookmarks.item import cli as item_cli
from bookmarks.group import cli as group_cli


@click.group()
def cli():
    pass


cli.add_command(init.command)
cli.add_command(item_cli.group)
cli.add_command(group_cli.group)
