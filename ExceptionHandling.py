server = {
    "name": "web-01",
    "cpu": 90
}

print(server["name"])
try:
    print(server["ip"])
except:
    print("IP address is not available")