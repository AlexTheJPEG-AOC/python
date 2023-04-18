player_score = 0

# Part 1
"""
values = {'A': 1,
          'B': 2,
          'C': 3,
          'X': 1,
          'Y': 2,
          'Z': 3}
while True:
    try:
        game = input().split()
        match game:
            case ['A', 'Z'] | ['B', 'X'] | ['C', 'Y']:
                player_score += values[game[1]]
            case ['A', 'Y'] | ['B', 'Z'] | ['C', 'X']:
                player_score += values[game[1]] + 6
            case ['A', 'X'] | ['B', 'Y'] | ['C', 'Z']:
                player_score += values[game[1]] + 3
    except EOFError:
        break
"""

# Part 2
lose = {'A': 'C',
        'B': 'A',
        'C': 'B'}
win = {'A': 'B',
       'B': 'C',
       'C': 'A'}
values = {'A': 1,
          'B': 2,
          'C': 3}
while True:
    try:
        game = input().split()
        match game[1]:
            case 'X':  # Need to lose
                player_score += values[lose[game[0]]]
            case 'Y':  # Need to draw
                player_score += values[game[0]] + 3
            case 'Z':  # Need to win
                player_score += values[win[game[0]]] + 6
    except EOFError:
        break

print(player_score)
