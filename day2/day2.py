import operator

with open('input.txt', 'r') as f:
    data = [int(x) for x in f.readline().strip().split(',')]


operations = {
    1: operator.add,
    2: operator.mul
}


def process_data(data: list) -> int:
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
    for noun in range(100):
        for verb in range(100):
            copy = data.copy()
            copy[1], copy[2] = noun, verb
            if process_data(copy) == 19690720:
                return noun, verb

noun, verb = find_pair()
print(f'Part 2: {noun*100 + verb}')
