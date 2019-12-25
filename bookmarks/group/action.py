import json

from bookmarks.group import repo


def list(dump_json):
    if dump_json:
        groups = []
        for g in repo.all():
            groups.append(g.to_dict())
        return json.dumps({'data': groups})
    else:
        result = ''
        for g in repo.all():
            result += '[{}] {}\n'.format(g.id, g.breadcrumb())
        return result


def add(**kwargs):
    return repo.add(**kwargs)


def delete(id_):
    return repo.remove(id_)
