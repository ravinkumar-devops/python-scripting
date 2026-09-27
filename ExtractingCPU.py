logs = [
    "INFO: web-01 application started",
    "WARNING: web-02 CPU usage is 72%",
    "ERROR: web-03 database connection failed",
    "WARNING: web-04 CPU usage is 91%",
    "INFO: web-05 health check passed",
    "WARNING: web-06 CPU usage is 86%"
]



def check_cpu(log_line, threshold=85):
        if "CPU" in log_line:
            list_of_strings = log_line.split()
            cpu_usage = int(list_of_strings[5].strip("%"))

            if cpu_usage >= threshold:
                current_utilization = "HIGH CPU"
            else:
                current_utilization = "NORMAL CPU"
            return {
                        "server": list_of_strings[1],
                        "cpu": cpu_usage, 
                        "status": current_utilization
            }

for log_line in logs:
        system_details = check_cpu(log_line, threshold=85)
        if system_details is not None:
              print(system_details)

# dict_of_logs = json
# print(type(dict_of_logs))

