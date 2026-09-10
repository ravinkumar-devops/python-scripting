import json

server = {
    "name": "web-01",
    "cpu": 75,
    "environment": "production"
}

converted_data = json.dumps(server)   #json string
server_dict = json.loads(converted_data) #dictionary

print(type(server_dict))

print(server_dict.get("name"))
print(server_dict.get("cpu"))