server = {
    "name": "web-01",
    "cpu": "90"
}

try:
    cpu = int(server["cpu"])
    print("CPU:", cpu)

    memory = int(server["memory"])
    print("Memory:", memory)

except KeyError:
    print("ERROR: Required field is missing")

except ValueError:
    print("ERROR: Invalid numeric value")

print("Program completed")

#output:

# CPU: 90
# ERROR: Required field is missing
# Program completed


# TRY
#  │
#  ├── Statement 1 ✅
#  │
#  ├── Statement 2 ✅
#  │
#  ├── Statement 3 ❌ Exception
#  │
#  X  STOP TRY BLOCK
#  │
#  ▼
# EXCEPT matching exception
#  │
#  ▼
# Continue program