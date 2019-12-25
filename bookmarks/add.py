import click

TYPES = ['path', 'command']
_DEFAULT_TYPE = TYPES[0]


@click.command(name='add')
@click.option(
    '--type',
    nargs=1,
    type=click.Choice(TYPES),
    default=_DEFAULT_TYPE,
    prompt=True
)
@click.option('--name', nargs=1, prompt=True)
@click.option('--value', nargs=1, prompt=True)
@click.option('--tag', 'tags', multiple=True, help='A comma separated list')
def command(type, name, value, tags):
    print(type, name, value, tags)
