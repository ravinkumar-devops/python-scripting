logs = [
    "INFO: web-01 application started",
    "ERROR: web-02 database connection failed",
    "WARNING: web-03 CPU usage is 89%",
    "ERROR: web-01 timeout connecting to database",
    "INFO: web-02 health check passed"
]

print(type(logs))

string_=(logs[1].split()[0]).strip(":")
print(string_)
print(logs[1].split()[1])

#split() -- converts string into list
#strip("chr") -- it will remove the chr under underscores 