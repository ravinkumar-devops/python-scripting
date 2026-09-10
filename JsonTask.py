import json

json_data = '''
{
    "instances": [
        {
            "id": "i-001",
            "name": "web-01",
            "cpu": 75
        },
        {
            "id": "i-002",
            "name": "web-02"
        },
        {
            "id": "i-003",
            "name": "web-03",
            "cpu": 95
        }
    ]
}
'''

py_dict = json.loads(json_data)

for instance in py_dict.get("instances"):
    print(instance.get("name"))
    
    