with open("day3input.txt", 'r') as file:
    directions = file.read()

position = [0, 0]
robo_position = [0, 0]
unique_positions = [[0, 0]]
robo_unique_positions = [[0, 0]]

for d in range(len(directions)):
    if directions[d] == '^':
        if d % 2 == 0:
            position[1] += 1
        else:
            robo_position[1] -= 1
    elif directions[d] == 'v':
        if d % 2 == 0:
            position[1] -= 1
        else:
            robo_position[1] += 1
    elif directions[d] == '<':
        if d % 2 == 0:
            position[0] -= 1
        else:
            robo_position[0] += 1
    elif directions[d] == '>':
        if d % 2 == 0:
            position[0] += 1
        else:
            robo_position[0] -= 1

    if position not in unique_positions:
        unique_positions.append(position.copy())
    if robo_position not in robo_unique_positions:
        robo_unique_positions.append(robo_position.copy())

print(f"{len(unique_positions) + len(robo_unique_positions) - 1} houses have received at least one present")
