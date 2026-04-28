import json

data = {"name": "Bogdan", "age": 31}

with open("data.json", "w") as file:
    json.dump(data, file)

with open("data.json", "r") as file:
    loaded = json.load(file)

print(loaded)