import json
import re

with open("input12.json", "r") as file:
    data = file.read()

numbers = [int(i) for i in re.findall(r"\-?\d+", data)]
print(sum(numbers))

with open("input12.json", "r") as file:
    data = json.load(file)


def check_for_red(obj):
    if isinstance(obj, dict):
        if "red" in obj.values():
            return 0
        return sum(check_for_red(obj[elem]) for elem in obj)
    elif isinstance(obj, list):
        return sum(check_for_red(elem) for elem in obj)
    else:
        if isinstance(obj, int):
            return obj
        if not obj.isdigit():
            return 0
        return int(obj)


print(check_for_red(data))