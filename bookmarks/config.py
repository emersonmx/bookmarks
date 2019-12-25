import os
import click

PATH = click.get_app_dir('bookmarks')


def setup():
    os.makedirs(PATH, exist_ok=True)
