log_line = "ERROR: web-01 CPU usage is 92%"

if "web-01" in log_line:
    print(log_line.split()[1])

if "ERROR" in log_line:
    print("Error detected")

lower_case=log_line.lower()

print(lower_case)

replaced_string=log_line.replace("ERROR", "CRITICAL")
print(replaced_string)

