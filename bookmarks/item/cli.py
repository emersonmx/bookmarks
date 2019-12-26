import json
import click

from bookmarks.item import action


@click.group(name='item')
def group():
    pass


@group.command()
@click.option('--dump-json', is_flag=True)
def list(dump_json):
    click.echo(action.list(dump_json))


@group.command()
@click.option('--name')
@click.option('--url')
@click.option('--group', 'group_id', type=int)
def add(name, url, group_id):
    b = action.add(name=name, url=url, group_id=group_id)
    click.echo('Bookmark "{}" with id {} was created'.format(b.name, b.id))


@group.command()
@click.argument('id_', metavar='ID')
def delete(id_):
    b = action.delete(id_)
    click.echo('Bookmark "{}" with id {} was deleted'.format(b.name, b.id))
