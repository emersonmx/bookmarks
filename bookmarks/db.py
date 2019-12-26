import os
import click

from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, scoped_session, relationship, backref
from sqlalchemy_mixins import AllFeaturesMixin

from bookmarks import config

_DATABASE_PATH = os.path.join(config.PATH, 'bookmarks.db')

_engine = create_engine('sqlite:///{}'.format(_DATABASE_PATH))
session_factory = sessionmaker(bind=_engine, autocommit=True)
Session = scoped_session(session_factory)
Base = declarative_base(cls=AllFeaturesMixin)
Base.set_session(Session())


@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except:  # noqa
        session.rollback()
        raise
    finally:
        session.close()


class Group(Base):
    __tablename__ = 'groups'
    __repr_attrs__ = ['name']
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    parent_id = Column(Integer, ForeignKey('groups.id'))

    children = relationship(
        'Group',
        backref=backref('parent', remote_side=[id]),
        cascade='all, delete-orphan'
    )
    bookmarks = relationship(
        'Bookmark', back_populates='group', cascade='all, delete-orphan'
    )

    def breadcrumb(self):
        def make(g):
            if g.parent_id:
                return make(g.parent) + ' > ' + g.name
            return g.name

        return make(self)


class Bookmark(Base):
    __tablename__ = 'bookmarks'
    __repr_attrs__ = ['name', 'url', 'group_id']
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    url = Column(String, nullable=False)
    group_id = Column(Integer, ForeignKey('groups.id'))

    group = relationship('Group', back_populates='bookmarks')


def setup():
    config.setup()

    if os.path.exists(_DATABASE_PATH):
        click.echo('Database exists!')
        return

    Base.metadata.create_all(_engine)
    Group.create(name='Bookmarks')

    click.echo('Database created!')
