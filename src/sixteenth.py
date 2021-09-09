import re

rule_range_pattern = re.compile(r'^(.*): (\d+)-(\d+) or (\d+)-(\d+)$')
rules = []
read_rules = False
newline_count = 0
invalid_numbers = []

with open('input/in16.txt') as f:
    for line in f:
        if line == '\n':
            newline_count += 1
            read_rules = True
            continue

        line = line.rstrip()
        if newline_count == 0:
            class_name, *rule_range = rule_range_pattern.findall(line)[0]
            rule_range = tuple(int(rule) for rule in rule_range)
            rules.append(rule_range)

        if newline_count == 2:
            if ':' in line:
                continue

            nums = [int(num) for num in line.split(',')]
            for num in nums:
                is_valid = False
                for min_a, max_a, min_b, max_b in rules:
                    if (min_a <= num <= max_a) or (min_b <= num <= max_b):
                        is_valid = True
                        break

                if not is_valid:
                    invalid_numbers.append(num)

    print(sum(invalid_numbers))
