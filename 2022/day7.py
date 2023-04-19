with open("input7.txt", "r") as file:
    cmd = file.read().splitlines()

current_dir = cmd[0].strip("$ cd")

ls = []
full_path = current_dir
dirs = {}
listing = False
for line in cmd[1:]:
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
            if not current_dir:
                current_dir = '/'
        else:
            current_dir = line[5:]
            full_path += f"{current_dir}/"
if ls:
    dirs[full_path] = ls

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
    sizes.append((k, size_of(dirs, k)))

small_dirs = [d for d in sizes if d[1] <= 100000]
print(sum([d[1] for d in small_dirs]))

outermost_size = sizes[0][1]
small_dirs = [d for d in sizes[1:] if 70000000 - outermost_size + d[1] >= 30000000]
print(min(small_dirs, key=lambda x: x[1])[1])
