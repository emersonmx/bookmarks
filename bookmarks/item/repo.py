from bookmarks import db


def all():
    with db.session_scope() as s:
        return s.query(db.Bookmark).all()


def add(**kwargs):
    with db.session_scope() as s:
        parent_id = kwargs.get('parent_id', None)
        g = db.Bookmark(name=kwargs.get('name'), parent_id=parent_id)
        s.add(g)
        s.flush()
        s.expunge(g)
        return g


def remove(gid):
    with db.session_scope() as s:
        g = s.query(db.Bookmark).get(gid)
        s.delete(g)
        return g
