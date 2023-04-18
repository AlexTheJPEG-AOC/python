part1_priority_sum = 0
part2_priority_sum = 0
values = list(' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
with open("input3.txt", "r") as file:
    rucksacks = file.read().splitlines()

for rucksack in rucksacks:
    first, second = set(rucksack[:len(rucksack)//2]), set(rucksack[len(rucksack)//2:])
    common = first.intersection(second)
    for element in common:
        part1_priority_sum += values.index(element)

rucksack_groups = [[set(rucksack) for rucksack in rucksacks[i:i+3]] for i in range(0, len(rucksacks), 3)]
for group in rucksack_groups:
    common = group[0].intersection(*group)
    for element in common:
        part2_priority_sum += values.index(element)

print(part1_priority_sum)
print(part2_priority_sum)