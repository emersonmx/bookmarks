from bookmarks import db


def all():
    with db.session_scope() as s:
        return s.query(db.Group).all()


def get_parents():
    with db.session_scope() as s:
        groups = s.query(db.Group).filter(db.Group.parent_id == None)  # noqa
        for o in groups:
            yield o


def add(**kwargs):
    with db.session_scope() as s:
        parent_id = kwargs.get('parent_id', None)
        g = db.Group(name=kwargs.get('name'), parent_id=parent_id)
        s.add(g)
        s.flush()
        s.expunge(g)
        return g


def remove(gid):
    with db.session_scope() as s:
        g = s.query(db.Group).get(gid)
        s.delete(g)
        return g
