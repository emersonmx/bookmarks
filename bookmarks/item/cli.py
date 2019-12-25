import click

from bookmarks.item import repo


@click.group(name='item')
def group():
    pass


@group.command()
def list():
    for b in repo.all():
        group = ''
        if b.group:
            group = ' {{{}}}'.format(b.group.name)
        click.echo('[{}] {} ({}){}'.format(b.id, b.name, b.url, group))


@group.command()
@click.option('--name')
@click.option('--url')
@click.option('--group', 'group_id', type=int)
def add(name, url, group_id):
    b = repo.add(name=name, url=url, group_id=group_id)
    click.echo('Bookmark "{}" with id {} was created'.format(b.name, b.id))


@group.command()
@click.argument('bookmark_id', metavar='ID')
def delete(bookmark_id):
    b = repo.remove(bookmark_id)
    click.echo('Bookmark "{}" with id {} was deleted'.format(b.name, b.id))
