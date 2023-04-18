def split_into_fours(s):
    l = []
    for char in range(0, len(s), 4):
        l.append(s[char : char + 4].strip())
    return l

# Get lines
crates = []
while True:
    line = input()
    if not line:
        break
    crates.append(split_into_fours(line))
del crates[-1]

# Create stacks
stacks = []
for index in range(len(crates[0])):
    stack = [row[index] for row in crates if row[index] != '']
    stack.reverse()
    stacks.append(stack)

# Do move operations
while True:
    try:
        op = input().split()
        m, f, t = [int(i) for i in op[1::2]]

        # Part 1
        # for _ in range(m):
        #    stacks[t - 1].append(stacks[f - 1].pop())

        # Part 2
        stacks[t - 1].extend(stacks[f - 1][-m:])
        del stacks[f - 1][-m:]

    except EOFError:
        break

for s in stacks:
    print(s)
print()

tops = [stack[-1] for stack in stacks]
print(tops)
