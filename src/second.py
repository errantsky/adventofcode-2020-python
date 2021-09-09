import re


counter = 0

with open('input/in2.txt') as f:
    for line in f:
        line = line.rstrip()
        pattern = re.compile(r'(\d+)-(\d+)\s(\w):\s(\w+)')
        min_count, max_count, character, password = pattern.match(line).groups()
        min_count, max_count = int(min_count), int(max_count)

        if password.count(character) >= min_count and password.count(character) <= max_count:
            counter += 1

print(counter)


