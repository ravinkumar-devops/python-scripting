import json

server = '''
{
    "name": "web-01",
    "environment": "production",
    "spec": {
        "cpu": 75,
        "memory": 80,
        "disk": {
            "size": 100,
            "type": "gp3"
        }
    }
}
'''

py_dict = json.loads(server)
print(py_dict)

print(py_dict.get("name"))
print(py_dict.get("environment"))
print(py_dict.get("spec").get("cpu"))
print(py_dict.get("spec").get("disk").get("size"))
print(py_dict.get("spec").get("disk").get("type"))