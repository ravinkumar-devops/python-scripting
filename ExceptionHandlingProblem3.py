server = {
    "name": "web-01",
    "cpu": "90"
}

try:
    cpu = int(server["cpu"])
    print("CPU:", cpu)

except KeyError:
    print("ERROR: Required field is missing")

else:
    print("Everything inside try worked successfully")

print("Program completed")

# try block
#    ↓
# cpu = int("90")
#    ↓
# Successful — no exception
#    ↓
# CPU: 90
#    ↓
# else block executes ✅
#    ↓
# Everything inside try worked successfully
#    ↓
# Program completed

#Note : else runs only when the try block completes successfully without any exception.| Situation        | `try`     | `except` | `else` |

