servers = ["server01", "server02", "server03", "server04", "server05", "server06"]

cpu_usage = [50,40,90]

for cpu in cpu_usage:
    if cpu > 85:
        print(f"WARNING: High cpu usage {cpu}%")
    else:
        print(f"CPU usage is normal: {cpu}%")

print("#################################")

for i in range(5):
    print(i)

print("#################################")

for i in range(1,6):
    print(i)

print("#################################")

for server_number in range(1,4):
    print(f"checking web-server-{server_number}")