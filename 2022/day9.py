with open("input9.txt", 'r') as file:
    directions = [line.strip().split() for line in file.readlines()]

# Part 1

h_pos = [0, 0]
old_h_pos = h_pos.copy()
t_pos = [0, 0]

t_unique_positions = set()
 
def t_is_close(pos):
    h_x = pos[0]
    h_y = pos[1]

    t_x = t_pos[0]
    t_y = t_pos[1]

    return abs(t_x - h_x) <= 1 and abs(t_y - h_y) <= 1


for item in directions:
    direction = item[0]
    amount = int(item[1])

    for i in range(amount):
        old_h_pos = h_pos.copy()

        match direction:
            case 'L':
                h_pos[0] -= 1
            case 'R':
                h_pos[0] += 1
            case 'U':
                h_pos[1] += 1
            case 'D':
                h_pos[1] -= 1

        if not t_is_close(h_pos):
            t_pos = old_h_pos.copy()

        t_unique_positions.add(tuple(t_pos))

print(len(t_unique_positions))

# Part 2

rope_pos = [[0, 0], [0, 0], [0, 0], [0, 0], 
            [0, 0], [0, 0], [0, 0], [0, 0],
            [0, 0], [0, 0]] 
old_pos = rope_pos.copy()

t_unique_positions = set()


def point_is_close(pos1, pos2):
    h_x = pos1[0]
    h_y = pos1[1]

    t_x = pos2[0]
    t_y = pos2[1]

    return abs(t_x - h_x) <= 1 and abs(t_y - h_y) <= 1


for item in directions[:10]:
    direction = item[0]
    amount = int(item[1])

    for i in range(amount):
        old_pos = rope_pos.copy()

        match direction:
            case 'L':
                rope_pos[0][0] -= 1
            case 'R':
                rope_pos[0][0] += 1
            case 'U':
                rope_pos[0][1] += 1
            case 'D':
                rope_pos[0][1] -= 1

        for knot in range(1, len(rope_pos)):
            if not point_is_close(rope_pos[knot], rope_pos[knot - 1]):
                print(old_pos)
                rope_pos[knot] = old_pos[knot - 1].copy()

        print(f"Going dir {direction} ({i+1} / {amount})")
        print(rope_pos)
        print()
