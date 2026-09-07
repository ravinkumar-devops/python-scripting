server1 = {
    "name": "web-01",
    "cpu": 92
}

server2 = {
    "name": "web-02",
    "cpu": 70
}


def check_server(server, threshold=85):
        # print(server.get("name"))

        if server.get("cpu") > threshold:
            status = f"{server.get("name")} ---> HIGH CPU"
        else:
            status = f"{server.get("name")} ---> Normal CPU"

        return server.get("name"), status

name1, status1 = check_server(threshold=34, server=server2)
name2, status2 = check_server(threshold=12, server=server1)

print(name1)
print(status1)

print(name2)
print(status2)