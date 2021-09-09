import re

rule_range_pattern = re.compile(r'^(.*): (\d+)-(\d+) or (\d+)-(\d+)$')
rules = []
read_rules = False
newline_count = 0
invalid_numbers = []
valid_tickets = []
class_names = []
my_ticket = []

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
            class_names.append(class_name)

        if newline_count == 1:
            if ':' in line:
                continue

            my_ticket = line.split(',')

        if newline_count == 2:
            if ':' in line:
                continue

            nums = [int(num) for num in line.split(',')]
            has_invalid_field = False

            for num in nums:
                is_valid = False
                for min_a, max_a, min_b, max_b in rules:
                    if (min_a <= num <= max_a) or (min_b <= num <= max_b):
                        is_valid = True
                        break

                if not is_valid:
                    invalid_numbers.append(num)
                    has_invalid_field = True

            if not has_invalid_field:
                valid_tickets.append([int(n) for n in line.split(',')])

    print(sum(invalid_numbers))

ordered_fields = [0] * len(class_names)
would_be = [{name: i for i, name in enumerate(class_names)} for j in range(len(valid_tickets[0]))]
for field_ind in range(len(valid_tickets[0])):
    for ticket in valid_tickets:
        field_val = int(ticket[field_ind])
        for i, (class_name, rule) in enumerate(zip(class_names, rules)):
            min_a, max_a, min_b, max_b = rule
            if not ((min_a <= field_val <= max_a) or (min_b <= field_val <= max_b)):
                if class_name in would_be[field_ind].keys():
                    would_be[field_ind].pop(class_name)


used = []

while not all(len(fi) == 1 for fi in would_be):
    for i, wb in enumerate(would_be):
        if len(wb) == 1:
            to_del = list(wb.keys())[0]
            for j in range(len(would_be)):
                if i != j:
                    if to_del in would_be[j]:
                        would_be[j].pop(to_del)

for thing in would_be:
    print(thing)

my_ticket = [int(n) for n in my_ticket]
acc = 1
for i, wb in enumerate(would_be):
    name, ind = list(wb.items())[0]
    if 'departure' in name:
        acc *= my_ticket[i]

print(acc)
