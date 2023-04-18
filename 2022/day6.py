stream = input()

# Values: 
# Packet: 4
# Message: 14
for i in range(len(stream) - 14):
    if sorted(list(stream[i:i+14])) == sorted(list(set(stream[i:i+14]))):
        print(f"First marker after character {i+14}")
        break
