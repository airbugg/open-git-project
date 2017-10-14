import json

from plumbum.cmd import locate, xargs

git_repo_locations = locate['/Users/eugenel/dev/**/.git'] | xargs['-I', '{}', 'dirname', '"{}"']

json_format = {"items": []}

for line in git_repo_locations().splitlines():
    json_format['items'].append({
        "uid": line,
        "title": '[{}] {}'.format(line.split('/')[4], line.split('/')[-1]),
        "subtitle": line,
        "arg": line,
        "icon": {"path": "icon.png"}
    })

print json.dumps(json_format)
