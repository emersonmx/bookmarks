import click

from bookmarks import db


@click.command(name='init')
def command():
    db.setup()
