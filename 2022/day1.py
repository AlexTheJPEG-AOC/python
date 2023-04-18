items = []
totals = []
with open("input1.txt", "r") as file:
    for item in file.read().splitlines():
        if item.isdigit():
            items.append(int(item))
        else:
            totals.append(sum(items))
            items = []

totals.sort(reverse=True)
print(totals[0])
print(sum(totals[:3]))
