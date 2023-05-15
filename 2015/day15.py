with open("input15.txt", "r") as file:
    lines = file.read().splitlines()

attributes = ["capacity", "durability", "flavor", "texture", "calories"]
ingredients = []
for line in lines:
    sp = line.split()
    values = (int(sp[2][:-1]), int(sp[4][:-1]), int(sp[6][:-1]),
              int(sp[8][:-1]), int(sp[10]))
    ingredients.append(dict(zip(attributes, values)))

# Exclude calories for part 1
del attributes[-1]

max_result_one = 0
max_result_two = 0
for first in range(101):
    for second in range(101 - first):
        for third in range(101 - first - second):
            coefficients = (first, second, third, 100 - first - second - third)
            result = 1
            for attr in attributes:
                result *= sum(coefficients[index] * ingredient[attr]
                              for index, ingredient in enumerate(ingredients))
                if result <= 0:
                    break
            if result > max_result_one:
                max_result_one = result
            if result > max_result_two and sum(coefficients[index] * ingredient["calories"] for index, ingredient in enumerate(ingredients)) == 500:
                max_result_two = result
print(max_result_one)
print(max_result_two)
