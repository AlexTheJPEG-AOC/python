import itertools

legend = dict()

with open("input9.txt", "r") as file:
    directions = file.read().splitlines()

for line in directions:
    match line.split():
        case [str(start), "to", str(dest), "=", str(dist)]:
            if start not in legend:
                legend[start] = dict()
            legend[start][dest] = int(dist)
            if dest not in legend:
                legend[dest] = dict()
            legend[dest][start] = int(dist)

cities = list(legend.keys())
route_dists = set()
for perm in itertools.permutations(cities, len(cities)):
    route_dist = 0
    for city in range(len(perm) - 1):
        route_dist += legend[perm[city]][perm[city+1]]
    route_dists.add(route_dist)
    
print(min(route_dists))
print(max(route_dists))