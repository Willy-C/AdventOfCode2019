import operator

with open('input.txt', 'r') as f:
    data_list = f.readline().strip().split(',')
    data = [int(x) for x in data_list]


operations = {
    1: operator.add,
    2: operator.mul
}


def process_data(data: list) -> list:
    for i in range(0, len(data), 4):
        opcode = data[i]
        if opcode in operations:
            data[data[i+3]] = operations[opcode](data[data[i+1]], data[data[i+2]])
        else:
            break
    return data[0]


print(f'Part 1: {process_data(data.copy())}')


# Part 2


def find_pair():
    for i in range(100):
        for j in range(100):
            copy = data.copy()
            copy[1], copy[2] = i, j
            if process_data(copy) == 19690720:
                return i, j


print(f'Part 2: {find_pair()}')
