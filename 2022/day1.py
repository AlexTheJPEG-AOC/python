items = []
totals = []
while True:
    try:
        item = input()
        if item.isdigit():
            items.append(int(item))
        else:
            totals.append(sum(items))
            items = []
    except EOFError:
        break

totals.sort(reverse=True)
print(totals[0])
print(sum(totals[:3]))
