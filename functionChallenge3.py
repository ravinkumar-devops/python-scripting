server1 = {
    "name": "web-01",
    "cpu": 92
}

server2 = {
    "name": "web-02",
    "cpu": 70
}


def check_server(server, threshold):
        # print(server.get("name"))

        if server.get("cpu") > threshold:
            status = "HIGH CPU"
        else:
            status = "Normal CPU"

        return server.get("name"), status

name1, status1 = check_server(server1, 85)
name2, status2 = check_server(server2, 85)

print(name1)
print(status1)

print(name2)
print(status2)