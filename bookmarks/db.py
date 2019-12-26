import os
import click

from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, scoped_session, relationship, backref

from bookmarks import config

_DATABASE_PATH = os.path.join(config.PATH, 'bookmarks.db')

_engine = create_engine('sqlite:///{}'.format(_DATABASE_PATH))
session_factory = sessionmaker(bind=_engine)
Session = scoped_session(session_factory)
Base = declarative_base()


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

    def to_dict(self, **kwargs):
        result = {'id': self.id, 'name': self.name}
        if self.parent:
            if kwargs.get('eager', False):
                result['parent'] = self.parent.to_dict()
            else:
                result['parent_id'] = self.parent_id
        if self.bookmarks:
            if kwargs.get('eager', False):
                result['bookmarks'] = list(
                    map(lambda o: o.to_dict(), self.bookmarks)
                )
        if self.children:
            if kwargs.get('eager', False):
                result['children'] = list(
                    map(lambda o: o.to_dict(), self.children)
                )
        return result

    def breadcrumb(self):
        def make(g):
            if g.parent_id:
                return make(g.parent) + ' > ' + g.name
            return g.name

        return make(self)


class Bookmark(Base):
    __tablename__ = 'bookmarks'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    url = Column(String, nullable=False)
    group_id = Column(Integer, ForeignKey('groups.id'))

    group = relationship('Group', back_populates='bookmarks')

    def to_dict(self, **kwargs):
        result = {'id': self.id, 'name': self.name, 'url': self.url}
        if self.group:
            if kwargs.get('eager', False):
                result['group'] = self.group.to_dict()
            else:
                result['group_id'] = self.group_id
        return result


def setup():
    config.setup()

    if os.path.exists(_DATABASE_PATH):
        click.echo('Database exists!')
        return

    Base.metadata.create_all(_engine)
    with session_scope() as session:
        group = Group(name='Bookmarks')
        session.add(group)

    click.echo('Database created!')
