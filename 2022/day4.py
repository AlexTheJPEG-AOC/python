contained_ranges = 0
overlapped_ranges = 0
while True:
    try:
        first, second = [i.split('-') for i in input().split(',')]
        first_range = range(int(first[0]), int(first[1]) + 1)
        second_range = range(int(second[0]), int(second[1]) + 1)
        if any([i in first_range for i in second_range]) or any([i in second_range for i in first_range]):
            overlapped_ranges += 1
            if all([i in first_range for i in second_range]) or all([i in second_range for i in first_range]):
                contained_ranges += 1
    except EOFError:
        break

print(f"Completely contained: {contained_ranges}")
print(f"Overlapping ranges:   {overlapped_ranges}")
