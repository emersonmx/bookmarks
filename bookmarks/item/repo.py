from bookmarks import db


def all():
    return db.Bookmark.all()


def add(**kwargs):
    return db.Bookmark.create(**kwargs)


def delete(id_):
    b = db.Bookmark.find_or_fail(id_)
    b.delete()
    return b
