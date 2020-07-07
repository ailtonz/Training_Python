import json

with open('links.json') as jsonfile:
    parsed = json.load(jsonfile)

print json.dumps(parsed, indent=2, sort_keys=True)