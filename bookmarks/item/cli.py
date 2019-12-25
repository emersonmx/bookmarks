import click

from bookmarks.item import repo


@click.group(name='item')
def group():
    pass


@group.command()
def list():
    for i in repo.all():
        click.echo(i.name)
