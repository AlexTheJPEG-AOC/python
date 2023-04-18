priority_sum = 0
values = list(' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

# Part 1
"""
while True:
    try:
        rucksack = input()
        first, second = set(rucksack[:len(rucksack)//2]), set(rucksack[len(rucksack)//2:])
        common = first.intersection(second)
        for element in common:
            priority_sum += values.index(element)
    except EOFError:
        break
"""

# Part 2
while True:
    try:
        rucksacks = [set(input()) for i in range(3)]
        common = rucksacks[0].intersection(*rucksacks)
        for element in common:
            priority_sum += values.index(element)
    except EOFError:
        break

print(priority_sum)
