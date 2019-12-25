import click

from bookmarks import init, group


@click.group()
def cli():
    pass


cli.add_command(init.command)
cli.add_command(group.group)
