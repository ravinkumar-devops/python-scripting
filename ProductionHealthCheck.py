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

server_details = json.loads(json_data)

for instance in server_details.get("instances"):
    print(instance.get("name"))
    cpu = instance.get("cpu") 
    memory = instance.get("memory")
    disk = instance.get("disk") 

    print(type(memory))

    if cpu is None:
        print("cpu is missing")
    elif cpu > 85:
        print("HIGH CPU")
    else:
        print("NORMAL CPU")
        
    if memory is None:
        print("missing memory")
    elif memory > 85:
        print("HIGH MEMORY")
    else:
        print("NORMAL memry")

    if disk is None:
        print("disk is missing")
    elif disk > 85:
        print("disk HIGH")
    else:
        print("NORMAL DISK")


