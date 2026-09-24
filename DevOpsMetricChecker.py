import json

json_data = '''
{
    "instances": [
        {
            "id": "i-001",
            "name": "web-01",
            "cpu": 75,
            "memory": 65,
            "disk": 70
        },
        {
            "id": "i-002",
            "name": "web-02",
            "cpu": 92,
            "disk": 60
        },
        {
            "id": "i-003",
            "name": "web-03",
            "cpu": 60,
            "memory": 55
        }
    ]
}
'''
#parsing JSON into python object
python_obj=json.loads(json_data)
print(type(python_obj))

#Looping though each instance

# print(python_obj)
print(python_obj.get("instances")[0].get("id"))

# for instance in instances[0].get("id")
def check_metric(value, threshold=85):
        if value is None:
            return "MISSING"
        elif value > threshold:
            return "HIGH"
        else:
            return "NORMAL"


for instance in python_obj.get("instances"):
    inst_name=instance.get("name")
    cpu_usage=instance.get("cpu")
    memory_usage=instance.get("memory")
    disk_usage=instance.get("disk")

cpu_info=check_metric(cpu_usage)
print(cpu_info)
        