import json

from bookmarks.item import repo


def list(dump_json):
    bookmarks = repo.all()
    if dump_json:
        result = []
        for b in bookmarks:
            result.append(b.to_dict())
        return json.dumps({'data': result})
    else:
        result = ''
        for b in bookmarks:
            bookmark = ' {{{}}}'.format(b.group.name) if b.group else ''
            result += '[{}] {} ({}){}\n'.format(b.id, b.name, b.url, bookmark)
        return result


def add(**kwargs):
    return repo.add(**kwargs)


def delete(id_):
    return repo.remove(id_)
