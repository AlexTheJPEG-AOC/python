def surface_area(length, width, height):
    return 2 * length * width + 2 * width * height + 2 * height * length


def smallest_side_area(length, width, height):
    return min(length * width, width * height, height * length)


def smallest_perimeter(length, width, height):
    return min(2 * length + 2 * width, 2 * width + 2 * height,
               2 * height + 2 * length)


def volume(length, width, height):
    return length * width * height


wrapping_paper = 0
ribbon = 0

with open("input2.txt", "r") as file:
    while line := file.readline():
        size = [int(dim) for dim in line.split('x')]
        wrapping_paper += surface_area(*size) + smallest_side_area(*size)
        ribbon += smallest_perimeter(*size) + volume(*size)

print(wrapping_paper, ribbon, sep='\n')
