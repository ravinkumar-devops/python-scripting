server1 = {
    "name": "web-01",
    "cpu": 92
}

def checkserver(server):
    print(f"checking {server["name"]}")
    if server.get("cpu") > 85:
        print("HIGH CPU")
    else:
        print("Normal CPU")

checkserver(server1)


    