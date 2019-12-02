import operator

with open('input.txt', 'r') as f:
    data_list = f.readline().strip().split(',')
    _data = [int(x) for x in data_list]


operations = {
    1: operator.add,
    2: operator.mul
}


def process_code(index: int, data):
    opcode = data[index]
    if opcode in operations:
        data[data[index + 3]] = operations[opcode](data[data[index + 1]], data[data[index + 2]])
    else:
        return


def process_data(data: list) -> list:
    for i in range(0, len(data), 4):
        process_code(i, data)
    return data[0]


print(f'Part 1: {process_data(_data.copy())}')


# Part 2


def find_pair():
    for i in range(100):
        for j in range(100):
            copy = _data.copy()
            copy[1], copy[2] = i, j
            if process_data(copy) == 19690720:
                return i, j


print(f'Part 2: {find_pair()}')
