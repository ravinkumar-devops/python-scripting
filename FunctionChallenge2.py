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
            return f"{server.get("name")} -> HIGH CPU"
        else:
            return f"{server.get("name")} -> NORMAL CPU"

status_server_1 = check_server(server1, 85)
status_server_2 = check_server(server2, 45)

print(status_server_1)
print(status_server_2)