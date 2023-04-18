def split_into_crates(s):
    l = []
    for char in range(0, len(s), 4):
        l.append(s[char : char + 4].strip("[] "))
    return l


crates = []
with open("input5.txt", "r") as file:
    lines = file.read().splitlines()

blank_line = lines.index("")
crate_diagram = lines[:blank_line]
instructions = lines[blank_line+1:]
# Get lines
for line in crate_diagram:
    crates.append(split_into_crates(line))

# Create stacks
part1_stacks = []
part2_stacks = []
for index in range(len(crates[0])):
    stack = [row[index] for row in crates if row[index] != '']
    stack.reverse()
    part1_stacks.append(stack)
    part2_stacks.append(stack.copy())

# Do move operations
for line in instructions:
    op = line.split()
    m, f, t = [int(i) for i in op[1::2]]

    # Part 1
    for _ in range(m):
       part1_stacks[t - 1].append(part1_stacks[f - 1].pop())

    # Part 2
    part2_stacks[t - 1].extend(part2_stacks[f - 1][-m:])
    del part2_stacks[f - 1][-m:]

print("".join([stack[-1] for stack in part1_stacks]))
print("".join([stack[-1] for stack in part2_stacks]))
