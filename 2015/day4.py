import hashlib

with open("input4.txt", "r") as file:
    secret_key = file.read()

number = 1
while not (hash := hashlib.md5(
        f"{secret_key}{number}".encode())).hexdigest().startswith("00000"):
    number += 1
print(number)
while not (hash := hashlib.md5(
        f"{secret_key}{number}".encode())).hexdigest().startswith("000000"):
    number += 1
print(number)
