import json

json_data = '''
{
    "name": "web-01",
    "environment": "production",
    "cpu": 75
}
'''

print(type(json_data))

server = json.loads(json_data)
print(type(server))
print(server)