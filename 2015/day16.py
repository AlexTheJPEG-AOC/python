import re

sues = []
with open("input16.txt", "r") as file:
    for line in file.read().splitlines():
        m = re.search("Sue \d+: (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)",
                      line)
        sue = m.groups()
        sues.append({
            sue[0]: int(sue[1]),
            sue[2]: int(sue[3]),
            sue[4]: int(sue[5]),
        })

target_sue = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


def check_item(sue, item, part2):
    if part2:
        if item in ("cats", "trees"):
            return sue[item] > target_sue[item]
        elif item in ("pomeranians", "goldfish"):
            return sue[item] < target_sue[item]
    return sue[item] == target_sue[item]


for index, sue in enumerate(sues):
    if all(check_item(sue, item, False) for item in sue):
        print(index + 1)
        break

for index, sue in enumerate(sues):
    if all(check_item(sue, item, True) for item in sue):
        print(index + 1)
        break
