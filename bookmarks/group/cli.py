import json
import click

from bookmarks.group import repo


@click.group(name='group')
def group():
    pass


@group.command()
@click.option('--dump-json', is_flag=True)
def list(dump_json):
    if dump_json:
        result = []
        for g in repo.all():
            result.append(g.to_dict())
        click.echo(json.dumps(result))
    else:
        for g in repo.all():
            click.echo('[{}] {}'.format(g.id, g.name))


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
