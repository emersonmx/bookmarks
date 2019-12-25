from setuptools import setup, find_packages

setup(
    name='bookmarks',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['Click', 'SQLAlchemy'],
    entry_points='''
        [console_scripts]
        bookmarks=bookmarks.cli:cli
    '''
)
