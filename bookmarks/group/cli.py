import click

from bookmarks.group import action


@click.group(name='group')
def group():
    pass


@group.command()
@click.option('--dump-json', is_flag=True)
def list(dump_json):
    click.echo(action.list(dump_json))


@group.command()
@click.option('--parent', type=int)
@click.argument('name')
def add(name, parent):
    g = action.add(name=name, parent_id=parent)
    click.echo('Group "{}" with id {} was created'.format(g.name, g.id))


@group.command()
@click.argument('id_', metavar='ID')
def delete(id_):
    g = action.delete(id_)
    click.echo('Group "{}" with id {} was deleted'.format(g.name, g.id))
