def calculate_fuel(mass: int) -> int:
    return mass // 3 - 2


with open('input.txt', 'r') as f:
    total = sum(calculate_fuel(int(mass)) for mass in f)

print(f'Part 1: {total}')


# Part 2


def fuel_with_fuel(mass: int) -> int:
    fuel_needed = 0
    while mass > 0:
        mass = calculate_fuel(mass)
        fuel_needed += max(mass, 0)
    return fuel_needed


with open('input.txt', 'r') as f:
    total2 = sum(fuel_with_fuel((int(mass))) for mass in f)

print(f'Part 2: {total2}')
