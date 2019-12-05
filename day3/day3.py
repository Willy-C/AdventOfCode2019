with open('input.txt', 'r') as f:
    wires = [[(path[0], int(path[1:])) for path in wire.split(',')] for wire in f.readlines()]


def get_coords(wire) -> list:
    x, y = 0, 0
    coords = []
    for step in wire:
        for _ in range(step[1]):
            if step[0] == 'U':
                y += 1
            elif step[0] == 'D':
                y -= 1
            elif step[0] == 'R':
                x += 1
            elif step[0] == 'L':
                x -= 1
            coords.append((x, y))
    return coords


coords1 = get_coords(wires[0])
coords2 = get_coords(wires[1])
intersects = set(coords1).intersection(coords2)

# Shortest Manhattan distance from central point
closest_intersection = (min([abs(x) + abs(y) for x, y in intersects]))
print(f'Part 1: {closest_intersection}')


# Part 2


def find_distance_to_intersect():
    steps = []
    for intr in intersects:
        steps1 = coords1.index(intr) + 1
        steps2 = coords2.index(intr) + 1
        steps.append(steps1+steps2)

    return min(steps)


# Fewest combined step to intersection
print(f'Part 2: {find_distance_to_intersect()}')
