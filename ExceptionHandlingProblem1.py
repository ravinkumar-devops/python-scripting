# server = {
#     "name": "web-01",
#     "cpu": 90
# }

# print(server.get("ip")) 

# try:
#     print(server["ip"])
# except KeyError:
#     print("IP address not avaiable")

server = {
    "name": "web-01",
    "cpu": 90
}

try:
    print(server["ip"])
    print("Checking CPU")   #this block will be never checked.
    
except KeyError:
    print("IP address not available")

print("Program completed")