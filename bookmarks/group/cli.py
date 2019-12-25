import click

from bookmarks.group import repo


@click.group(name='group')
def group():
    pass


@group.command()
def list():
    for g in repo.get_parents():
        _list_group(g)


@group.command()
@click.option('--parent', type=int)
@click.argument('name')
def add(name, parent):
    g = repo.add(name=name, parent_id=parent)
    click.echo('Group "{}" with id {} was created'.format(g.name, g.id))


@group.command()
@click.argument('group_id', metavar='ID')
def delete(group_id):
    g = repo.remove(group_id)
    click.echo('Group "{}" with id {} was deleted'.format(g.name, g.id))


def _list_group(g, i=0):
    indent = '    ' * i
    click.echo('{}[{}] {}'.format(indent, g.id, g.name))
    for c in g.children:
        _list_group(c, i + 1)
