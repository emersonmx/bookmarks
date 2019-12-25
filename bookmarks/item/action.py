import json

from bookmarks.item import repo


def list(dump_json):
    if dump_json:
        bookmarks = []
        for g in repo.all():
            bookmarks.append(g.to_dict())
        return json.dumps({'data': bookmarks})
    else:
        result = ''
        for g in repo.all():
            group = ' {{{}}}'.format(g.group.name) if g.group else ''
            result += '[{}] {} ({}){}\n'.format(g.id, g.name, g.url, group)
        return result


def add(**kwargs):
    return repo.add(**kwargs)


def delete(id_):
    return repo.remove(id_)
