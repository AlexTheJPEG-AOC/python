import itertools

with open("input10.txt", "r") as file:
    digits = file.read()

for _ in range(40):
    groups = [f"{len(list(g))}{k}" for k, g in itertools.groupby(digits)]
    digits = "".join(groups)
print(len(digits))
for _ in range(10):
    groups = [f"{len(list(g))}{k}" for k, g in itertools.groupby(digits)]
    digits = "".join(groups)
print(len(digits))