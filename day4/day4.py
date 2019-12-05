from collections import Counter

with open('input.txt', 'r') as f:
    lower, upper = (int(num) for num in f.read().split('-'))


def is_valid_pw(pw):
    pw = str(pw)
    return all(i <= j for i, j in zip(pw, pw[1:])) and any(i == j for i, j in zip(pw, pw[1:]))


count = sum(is_valid_pw(pw) for pw in range(lower, upper + 1))
print(f'Part 1: {count}')


# Part 2


def is_valid_pw2(pw):
    pw = str(pw)
    freqs = Counter(pw)
    return all(i <= j for i, j in zip(pw, pw[1:])) and any(freq == 2 for freq in freqs.values())


count2 = sum(is_valid_pw2(pw) for pw in range(lower, upper + 1))
print(f'Part 2: {count2}')
