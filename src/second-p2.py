import re


counter = 0

with open('input/in2.txt') as f:
    for line in f:
        line = line.rstrip()
        pattern = re.compile(r'(\d+)-(\d+)\s(\w):\s(\w+)')
        first_ind, second_ind, character, password = pattern.match(line).groups()
        first_ind, second_ind = int(first_ind) - 1, int(second_ind) - 1
        
        if (password[first_ind] == character) ^ (password[second_ind] == character):
            counter += 1



print(counter)


