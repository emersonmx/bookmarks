from bookmarks import db


def all():
    with db.session_scope() as s:
        for o in s.query(db.Bookmark).all():
            yield o


def add(**kwargs):
    with db.session_scope() as s:
        group_id = kwargs.get('group_id', None)
        b = db.Bookmark(
            name=kwargs.get('name'),
            value=kwargs.get('value'),
            group_id=group_id
        )
        s.add(b)
        s.flush()
        s.expunge(b)
        return b


def remove(bid):
    with db.session_scope() as s:
        b = s.query(db.Bookmark).get(bid)
        s.delete(b)
        return b
