with open("input9.txt", 'r') as file:
    instructions = [line.split() for line in file.read().splitlines()]


def points_are_close(p1, p2):
    return abs(p2[0] - p1[0]) <= 1 and abs(p2[1] - p1[1]) <= 1

# Part 1
head_pos = [0, 0]
tail_pos = [0, 0]
unique_tail_pos = set()
for direction, times in instructions:
    for _ in range(int(times)):
        if direction == 'L':
            head_pos[0] -= 1
        elif direction == 'R':
            head_pos[0] += 1
        elif direction == 'U':
            head_pos[1] += 1
        else:
            head_pos[1] -= 1
        if not points_are_close(head_pos, tail_pos):
            if direction == 'L':
                tail_pos = [head_pos[0] + 1, head_pos[1]]
            elif direction == 'R':
                tail_pos = [head_pos[0] - 1, head_pos[1]]
            elif direction == 'U':
                tail_pos = [head_pos[0], head_pos[1] - 1]
            else:
                tail_pos = [head_pos[0], head_pos[1] + 1]
            unique_tail_pos.add(tuple(tail_pos))

print(len(unique_tail_pos))

# Part 2
rope_pos = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
unique_tail_pos = set()
for direction, times in instructions:
    for _ in range(int(times)):
        if direction == 'L':
            rope_pos[0][0] -= 1
        elif direction == 'R':
            rope_pos[0][0] += 1
        elif direction == 'U':
            rope_pos[0][1] += 1
        else:
            rope_pos[0][1] -= 1
        for pos in range(1, len(rope_pos)):
            if not points_are_close(rope_pos[pos], rope_pos[pos - 1]):
                if direction == 'L':
                     = [head_pos[0] + 1, head_pos[1]]
                elif direction == 'R':
                    tail_pos = [head_pos[0] - 1, head_pos[1]]
                elif direction == 'U':
                    tail_pos = [head_pos[0], head_pos[1] - 1]
                else:
                    tail_pos = [head_pos[0], head_pos[1] + 1]
                