import click

from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, backref

_engine = create_engine('sqlite:///bookmarks.db')
Session = sessionmaker(bind=_engine)


@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except:  # noqa E722
        session.rollback()
        raise
    finally:
        session.close()


Base = declarative_base()


def setup():
    Base.metadata.create_all(_engine)
    with session_scope() as session:
        group = Group(name='Root')
        session.add(group)

    click.echo('Database created')


class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    parent_id = Column(Integer, ForeignKey('groups.id'))

    children = relationship(
        'Group', backref=backref('parent', remote_side=[id])
    )
    bookmarks = relationship('Bookmark', back_populates='group')


class Bookmark(Base):
    __tablename__ = 'bookmarks'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    value = Column(String, nullable=False)
    group_id = Column(Integer, ForeignKey('groups.id'), nullable=False)

    group = relationship('Group', back_populates='bookmarks')
