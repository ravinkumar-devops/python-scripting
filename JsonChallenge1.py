import json

json_data = '''
{
    "name": "web-01",
    "environment": "production",
    "cpu": 75,
    "memory": 80
}
'''
#Convert json_data into a Python dictionary using json.loads()

converted_dict = json.loads(json_data)
print(type(converted_dict))

print(converted_dict.get("name"))
print(converted_dict.get("cpu"))
print(converted_dict.get("memory"))


if converted_dict.get("cpu") > 70:
    print("High cpu")
else:
    print("Normal CPU")