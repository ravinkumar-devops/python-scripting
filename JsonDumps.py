import json

server = {
    "name": "web-01",
    "cpu": 75,
    "environment": "production"
}

converted_data = json.dumps(server)

print(converted_data)
print(type(converted_data))

print(converted_data["name"])