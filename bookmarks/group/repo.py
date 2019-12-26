from bookmarks import db


def all():
    return db.Group.all()


def add(**kwargs):
    return db.Group.create(**kwargs)


def delete(id_):
    g = db.Group.find_or_fail(id_)
    g.delete()
    return g
