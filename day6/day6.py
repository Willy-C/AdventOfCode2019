with open('input.txt', 'r') as f:
    data = [line.strip('\n') for line in f]

mp = {}

for orbit in data:
    inner, outer = orbit.split(')')
    if outer not in mp:
        mp[outer] = inner


def count_orbits(key):
    v = mp[key]
    counter = 1
    while v in mp:
        v = mp[v]
        counter += 1
    return counter


counter = 0
for k in mp:
    counter += count_orbits(k)

print(f'Part 1: {counter}')


# Part 2


def get_path(key):
    v = mp[key]
    path = []
    while v in mp:
        path.append(v)
        v = mp[v]
    return path


path1 = get_path('YOU')
path2 = get_path('SAN')

inter = set(path1).intersection(path2)

path_length = len(path1) + len(path2) - len(inter) * 2
print(f'Part 2: {path_length}')
