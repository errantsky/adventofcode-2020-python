from itertools import combinations


with open('input/in1.txt') as f:
    lines = f.readlines()

ls = [line.rstrip() for line in lines]


for a, b, c in combinations(ls, 3):
    a, b, c = int(a), int(b), int(c)
    if a + b + c == 2020:
        print(a * b * c)



