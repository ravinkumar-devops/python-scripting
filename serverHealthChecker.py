server_name = "web-server-01"
cpu_usage = 95
memory_usage = 90
server_running = True

if not server_running:
    print("CRITICAL: Server is DOWN")
elif cpu_usage > 80:
    print("WARNING: High CPU usage")
elif memory_usage > 80:
    print("WARNING: High memory usage")
else:
    print("Server health is NORMAL")


#Note : output shown here is wrong because cpu_usage and memory_usage both are high but it just checked the cpu_usage and came outside of the conditional chain.


print("######################################")

if not server_running:
    print("CRITICAL: Server is DOWN")
if cpu_usage > 80:
    print("WARNING: High CPU usage")
if memory_usage > 80:
    print("WARNING: High memory usage")
