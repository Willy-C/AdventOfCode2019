import operator

with open('input.txt', 'r') as f:
    data = [int(x) for x in f.readline().strip().split(',')]

operations = {
    1: operator.add,
    2: operator.mul
}

def process_data(data: list, _input):
    i = 0
    while i < len(data):
        instruction = str(data[i]).zfill(5)
        opcode = int(instruction[-2:])

        if opcode in operations:
            param1 = data[data[i + 1]] if instruction[-3] == '0' else data[i + 1]
            param2 = data[data[i + 2]] if instruction[-4] == '0' else data[i + 2]
            data[data[i + 3]] = operations[opcode](param1, param2)
            i += 4
        elif opcode == 3:
            data[data[i + 1]] = _input
            i += 2
        elif opcode == 4:
            print(f'Opcode 4: {data[data[i + 1]] if instruction[-3] == "0" else data[i + 1]}')
            i += 2
        elif opcode in (5, 6):
            param1 = data[data[i + 1]] if instruction[-3] == '0' else data[i + 1]
            param2 = data[data[i + 2]] if instruction[-4] == '0' else data[i + 2]

            if (param1 != 0 and opcode == 5) or (param1 == 0 and opcode == 6):
                i = param2
            else:
                i += 3
        elif opcode == 7:
            param1 = data[data[i + 1]] if instruction[-3] == '0' else data[i + 1]
            param2 = data[data[i + 2]] if instruction[-4] == '0' else data[i + 2]

            if param1 < param2:
                data[data[i + 3]] = 1
            else:
                data[data[i + 3]] = 0
            i += 4
        elif opcode == 8:
            param1 = data[data[i + 1]] if instruction[-3] == '0' else data[i + 1]
            param2 = data[data[i + 2]] if instruction[-4] == '0' else data[i + 2]

            if param1 == param2:
                data[data[i + 3]] = 1
            else:
                data[data[i + 3]] = 0
            i += 4
        elif opcode == 99:
            break
        else:
            print(f'Unknown Opcode: {opcode}')
            break


print('Part 1:')
process_data(data.copy(),1 )
print(f'{"-" * 20}\nPart 2:')
process_data(data.copy(), 5)

