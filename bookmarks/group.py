import click

from bookmarks import db


@click.group()
def group():
    pass


@group.command()
@click.option('--parent', type=int)
@click.argument('name')
def add(name, parent):
    with db.session_scope() as s:
        g = db.Group(name=name, parent_id=parent)
        s.add(g)
        s.flush()
        click.echo('Group "{}" created with id {}'.format(g.name, g.id))


@group.command()
def list():
    with db.session_scope() as s:
        groups = s.query(db.Group)\
            .filter(db.Group.parent_id == None)  # noqa
        for g in groups:
            _list_group(g)


def _list_group(g, i=0):
    indent = '    ' * i
    click.echo('{}[{}] {}'.format(indent, g.id, g.name))
    for c in g.children:
        _list_group(c, i + 1)
