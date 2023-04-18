current_dir = input().strip("$ cd")

ls = []
full_path = current_dir
dirs = {}
listing = False
while True:
    try:
        line = input()
        if listing:
            if line[0] == '$':
                listing = False
                dirs[full_path] = ls
                ls = []
            else:
                ls.append(line)
        if line == "$ ls":
            listing = True
        elif line.startswith("$ cd "):
            if line.endswith(".."):
                current_dir = full_path.split('/')[-2]
                full_path = full_path[:-(len(current_dir) + 1)]
                current_dir = full_path.split('/')[-2]
                # current_dir = full_path.rsplit('/', 1)[0].strip('/')
                if not current_dir:
                    current_dir = '/'
            else:
                current_dir = line[5:]
                full_path += f"{current_dir}/"
    except EOFError:
        if ls:
            dirs[full_path] = ls
        break

def size_of(dirs, dirname):
    size = 0
    for item in dirs[dirname]:
        if item[0].isdigit():
            size += int(item.split()[0])
        else:
            size += size_of(dirs, dirname + item.split()[-1] + '/')
    return size

sizes = [] 
for k in dirs.keys():
    # print(k, dirs[k])
    sizes.append((k, size_of(dirs, k)))

small_dirs = [d for d in sizes if d[1] <= 100000]
# print(small_dirs)
print(sum([d[1] for d in small_dirs]))

outermost_size = sizes[0][1]
small_dirs = [d for d in sizes[1:] if 70000000 - outermost_size + d[1] >= 30000000]
print(min(small_dirs, key=lambda x: x[1])[1])
