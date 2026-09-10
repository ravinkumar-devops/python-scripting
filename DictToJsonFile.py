import json
from pathlib import Path

server = {
    "name": "web-02",
    "environment": "staging",
    "cpu": 65,
    "memory": 70
}

Target_File=Path.cwd() / "server_output.json"
print(Target_File)

with open(Target_File,"w") as f:
    json.dump(server, f, indent=4)    

f.close()

print(Target_File)
