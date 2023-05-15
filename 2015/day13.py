import itertools

legend = dict()

with open("input13.txt", "r") as file:
    seatings = file.read().splitlines()

for seating in seatings:
    person1, _, rest = seating.partition(" ")
    _, lose_gain, happiness, *rest = rest.split(" ")
    person2 = rest[-1][:-1]
    happiness = int(happiness)
    if lose_gain == "lose":
        happiness *= -1

    if person1 not in legend:
        legend[person1] = dict()
    legend[person1][person2] = happiness


def find_max_happiness():
    people = list(legend.keys())
    table_happinesses = set()
    for perm in itertools.permutations(people, len(people)):
        happiness = 0
        for person in range(len(perm)):
            if person == len(perm) - 1:
                happiness += legend[perm[person]][perm[0]]
                happiness += legend[perm[0]][perm[person]]
            else:
                happiness += legend[perm[person]][perm[person + 1]]
                happiness += legend[perm[person + 1]][perm[person]]
        table_happinesses.add(happiness)

    return max(table_happinesses)


print(find_max_happiness())

people = list(legend.keys())
legend["Alex"] = dict()
for person in people:
    legend["Alex"][person] = 0
    legend[person]["Alex"] = 0
print(find_max_happiness())