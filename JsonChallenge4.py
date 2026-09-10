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
            "name": "web-02",
            "cpu": 90
        },
        {
            "id": "i-003",
            "name": "web-03",
            "cpu": 60
        }
    ]
}
'''
dict_01=json.loads(json_data)

print(dict_01)

print(type(dict_01))

print(dict_01.get("instances")[0].get("name"))
print(dict_01.get("instances")[1].get("cpu"))

for instance in dict_01.get("instances"):
    print(instance.get("name"))

    if instance.get("cpu") > 85:
        print("HIGH CPU")
    else:
        print("NORMAL CPU")