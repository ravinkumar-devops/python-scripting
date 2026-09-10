import json
from pathlib import Path

print(Path.cwd())

json_file_path = Path.cwd() / "server.json"
print(json_file_path)

with open(json_file_path,"r") as f:
    py_dict = json.load(f)

    print(type(py_dict))
    print(py_dict.get("name"))
    print(py_dict.get("cpu"))
    print(py_dict.get("memory"))