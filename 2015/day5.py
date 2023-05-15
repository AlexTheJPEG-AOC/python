def part1_is_nice(string):
    forbidden = {"ab", "cd", "pq", "xy"}
    vowels = "aeiou"

    vowel_count = 0
    three_plus_vowels = False
    for c in string:
        if c in vowels:
            vowel_count += 1
        if vowel_count == 3:
            three_plus_vowels = True
            break
    if not three_plus_vowels:
        return False

    twice_in_a_row = any(string[c] == string[c + 1]
                         for c in range(len(string) - 1))
    if not twice_in_a_row:
        return False

    contains_forbidden = any(f in string for f in forbidden)
    if contains_forbidden:
        return False

    return True


def part2_is_nice(string):
    two_letters = []
    two_letter_appears_twice = False
    for c in range(len(string) - 1):
        if (two_letter := string[c:c + 2]) in two_letters:
            if string[c - 1:c + 1] != two_letter:
                two_letter_appears_twice = True
                break
        two_letters.append(string[c:c + 2])
    if not two_letter_appears_twice:
        return False

    letter_sandwich = False
    for c in range(len(string) - 2):
        three_letter = string[c:c + 3]
        if three_letter[0] == three_letter[-1]:
            letter_sandwich = True
            break
    if not letter_sandwich:
        return False

    return True


with open("input5.txt", "r") as file:
    part1_nice = 0
    part2_nice = 0
    for line in file.read().splitlines():
        if part1_is_nice(line):
            part1_nice += 1
        if part2_is_nice(line):
            part2_nice += 1

print(part1_nice)
print(part2_nice)
