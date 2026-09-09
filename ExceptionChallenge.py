servers = [
    {"name": "web-01", "cpu": "75"},
    {"name": "web-02"},
    {"name": "web-03", "cpu": "ninety"},
    {"name": "web-04", "cpu": "60"}
]

for server in servers:
    try :
        cpu = int(server["cpu"])
    except KeyError:
        print(f"{server["name"]} -> CPU information missing")
    except ValueError:
        print(f"{server["name"]} -> Invalid CPU value")
    else:
        print(f"{server["name"]} -> CPU:{cpu}")