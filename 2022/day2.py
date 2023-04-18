part1_score = 0
part2_score = 0

values = {'A': 1,
          'B': 2,
          'C': 3,
          'X': 1,
          'Y': 2,
          'Z': 3}
part2_lose = {'A': 'C',
        'B': 'A',
        'C': 'B'}
part2_win = {'A': 'B',
       'B': 'C',
       'C': 'A'}

with open("input2.txt", "r") as file:
    for line in file.read().splitlines():
        game = line.split()
        match game:
            case ['A', 'Z'] | ['B', 'X'] | ['C', 'Y']:
                part1_score += values[game[1]]
            case ['A', 'Y'] | ['B', 'Z'] | ['C', 'X']:
                part1_score += values[game[1]] + 6
            case ['A', 'X'] | ['B', 'Y'] | ['C', 'Z']:
                part1_score += values[game[1]] + 3
        match game[1]:
            case 'X':  # Need to lose
                part2_score += values[part2_lose[game[0]]]
            case 'Y':  # Need to draw
                part2_score += values[game[0]] + 3
            case 'Z':  # Need to win
                part2_score += values[part2_win[game[0]]] + 6

print(part1_score)
print(part2_score)
