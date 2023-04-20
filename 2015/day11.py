alphabet = "abcdefghijklmnopqrstuvwxyz"


def pass_arr_to_number(password_arr):
    password_number = 0
    for index, number in enumerate(password_arr):
        password_number += number * (26**(len(password_arr) - index - 1))
    return password_number


def number_to_pass_arr(number):
    array = []
    while number:
        number, value = divmod(number, 26)
        array.append(value)
    array.reverse()
    return array


def pass_arr_to_string(password_arr):
    return "".join(alphabet[c] for c in password_arr)


def find_next_password(password_arr):
    password_number = pass_arr_to_number(password_arr)
    while True:
        password_number += 1
        password_arr = number_to_pass_arr(password_number)

        if 8 in password_arr or 11 in password_arr or 14 in password_arr:
            continue

        straight = False
        for i in range(len(password_arr) - 2):
            if password_arr[i] == password_arr[i + 1] - 1 == password_arr[
                    i + 2] - 2:
                straight = True
                break
        if not straight:
            continue

        pairs = 0
        letters = set()
        for i in range(len(password_arr) - 1):
            if password_arr[i] not in letters and password_arr[
                    i] == password_arr[i + 1]:
                pairs += 1
                letters.add(password_arr[i])
        if pairs < 2:
            continue

        break

    return pass_arr_to_string(password_arr)


with open("input11.txt", "r") as file:
    password = file.read()

password_arr = [alphabet.index(c) for c in password]
print(new_password := find_next_password(password_arr))
password_arr = [alphabet.index(c) for c in new_password]
print(find_next_password(password_arr))
