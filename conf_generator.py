import json

with open("volunteers.json", "r") as f:
    volunteers = json.load(f)

untis = ["C5-LUA", "C6-back", "D2-RUA", "D5-LC", "DE-Waist", "F5-RC"]
sensors = ["Accelerometer", "Gyroscope"]
dropped = ["epoc (ms)", "elapsed (s)"]

configurations = {}

for vol in volunteers:
    for path in volunteers[vol]:
        configurations[path] = {
            "units": untis,
            "sensors": sensors,
            "dropped": dropped,
            "out": path
        }

with open("experiment_config.json", "w") as f:
    json.dump(configurations, f)

print("Done")