with open("input8.txt", "r") as file:
    lines = file.read().splitlines()

code_chars = 0
mem_chars = 0
enc_chars = 0
for line in lines:
    code_chars += len(line)
    mem_chars += len(eval(line))
    for c in repr(line):
        enc_chars += 2 if c == '"' else 1

print(code_chars - mem_chars)
print(enc_chars - code_chars)