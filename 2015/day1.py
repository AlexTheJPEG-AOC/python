floor = 0
legend = {'(': 1, ')': -1}
basement_index = 0

with open("input1.txt", "r") as file:
    for i in range(len(instructions := file.readline())):
        floor += legend[instructions[i]]
        if not basement_index and floor == -1:
            basement_index = i + 1

print(floor, basement_index, sep='\n')
