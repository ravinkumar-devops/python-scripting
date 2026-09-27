logs = [
    "INFO: web-01 application started",
    "ERROR: web-02 database connection failed",
    "WARNING: web-03 CPU usage is 89%",
    "ERROR: web-01 timeout connecting to database",
    "INFO: web-02 health check passed"
]

# print(logs[0].split()[1])   #accessing server name

# finding the log_level and server name
for lines in logs:
    log_level = lines.split()[0].strip(":")
    server_name = lines.split()[1]
    print(f" { log_level } | {server_name} ")

    if "CPU" in lines:
        print(type(lines.split()[5].strip("%")))   #string
        cpu=int(lines.split()[5].strip("%"))


        print(cpu) #int
        print(type(cpu))   #int

        if cpu > 85:
            print("HIGH CPU")
        else:
            print("NORMAL CPU")