import click

from bookmarks import add, init


@click.group()
def cli():
    pass


cli.add_command(init.command)
cli.add_command(add.command)
