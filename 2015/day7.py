import functools

with open("input7.txt", "r") as file:
    instructions = file.read().splitlines()

MAX_INT = 0xFFFF
signals = dict()

for line in instructions:
    connect, to = line.split(" -> ")
    signals[to] = connect.split()

# for k, v in signals.items():
#     print(k, v, sep=" = ")


@functools.cache
def get_value(key):
    if key.isdigit():
        return int(key)
    value = signals[key]
    match value:
        case [str(wire)]:
            return get_value(wire)
        case ["NOT", str(wire)]:
            return MAX_INT - get_value(wire)
        case [str(wire1), "AND", str(wire2)]:
            return get_value(wire1) & get_value(wire2)
        case [str(wire1), "OR", str(wire2)]:
            return get_value(wire1) | get_value(wire2)
        case [str(wire1), "LSHIFT", str(wire2)]:
            return (get_value(wire1) << get_value(wire2)) & MAX_INT
        case [str(wire1), "RSHIFT", str(wire2)]:
            return get_value(wire1) >> get_value(wire2)


a_value = get_value("a")
print(a_value)

signals["b"] = [str(a_value)]
get_value.cache_clear()
print(get_value("a"))