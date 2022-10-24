import json

filename = 'data.json'
with open(filename) as f_obj:
    data = json.load(f_obj)

for key, value in data.items():
    sum = 0
    for val in value:
        if val is not None and val.isdigit():
            sum += int(val)

    print(key, sum)