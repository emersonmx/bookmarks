import json

from bookmarks.group import repo


def list(dump_json):
    groups = repo.all()
    if dump_json:
        result = []
        for g in groups:
            result.append(g.to_dict())
        return json.dumps({'data': result})
    else:
        result = ''
        for g in groups:
            result += '[{}] {}\n'.format(g.id, g.breadcrumb())
        return result


def add(**kwargs):
    return repo.add(**kwargs)


def delete(id_):
    return repo.remove(id_)
