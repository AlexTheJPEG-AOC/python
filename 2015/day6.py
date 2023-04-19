with open("input6.txt", "r") as file:
    instructions = file.read().splitlines()

part1_lights = [[False for _ in range(1000)] for _ in range(1000)]
part2_lights = [[0 for _ in range(1000)] for _ in range(1000)]

for line in instructions:
    if line.startswith("turn on"):
        bounds = line[8:].split(" through ")
        bounds = tuple(tuple(int(i) for i in b.split(',')) for b in bounds)
        for r in range(bounds[0][1], bounds[1][1] + 1):
            for c in range(bounds[0][0], bounds[1][0] + 1):
                part1_lights[r][c] = True
                part2_lights[r][c] += 1
    elif line.startswith("turn off"):
        bounds = line[9:].split(" through ")
        bounds = tuple(tuple(int(i) for i in b.split(',')) for b in bounds)
        for r in range(bounds[0][1], bounds[1][1] + 1):
            for c in range(bounds[0][0], bounds[1][0] + 1):
                part1_lights[r][c] = False
                part2_lights[r][c] -= 1
                if part2_lights[r][c] < 0:
                    part2_lights[r][c] = 0
    else:
        bounds = line[7:].split(" through ")
        bounds = tuple(tuple(int(i) for i in b.split(',')) for b in bounds)
        for r in range(bounds[0][1], bounds[1][1] + 1):
            for c in range(bounds[0][0], bounds[1][0] + 1):
                part1_lights[r][c] = not part1_lights[r][c]
                part2_lights[r][c] += 2

print(sum(r.count(True) for r in part1_lights))
print(sum(sum(r) for r in part2_lights))