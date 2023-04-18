part1_position = [0, 0]
part2_position = [0, 0]
robo_position = [0, 0]
part1_unique_positions = {(0, 0)}
part2_unique_positions = {(0, 0)}
robo_unique_positions = {(0, 0)}

with open("input3.txt", 'r') as file:
    for d in range(len(directions := file.readline())):
        if directions[d] == '^':
            part1_position[1] += 1
            if d % 2 == 0:
                part2_position[1] += 1
            else:
                robo_position[1] += 1
        elif directions[d] == 'v':
            part1_position[1] -= 1
            if d % 2 == 0:
                part2_position[1] -= 1
            else:
                robo_position[1] -= 1
        elif directions[d] == '<':
            part1_position[0] -= 1
            if d % 2 == 0:
                part2_position[0] -= 1
            else:
                robo_position[0] -= 1
        elif directions[d] == '>':
            part1_position[0] += 1
            if d % 2 == 0:
                part2_position[0] += 1
            else:
                robo_position[0] += 1

        part1_unique_positions.add(tuple(part1_position))
        part2_unique_positions.add(tuple(part2_position))
        robo_unique_positions.add(tuple(robo_position))

print(len(part1_unique_positions))
print(len(part2_unique_positions.union(robo_unique_positions)))
