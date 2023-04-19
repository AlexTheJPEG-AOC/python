with open("input6.txt", "r") as file:
    stream = file.read()

packets = [stream[i:i+4] for i in range(len(stream) - 3)]
messages = [stream[i:i+14] for i in range(len(stream) - 13)]
for index, packet in enumerate(packets):
    if sorted(list(packet)) == sorted(list(set(packet))):
        print(index + 4)
        break
for index, message in enumerate(messages):
    if sorted(list(message)) == sorted(list(set(message))):
        print(index + 14)
        break