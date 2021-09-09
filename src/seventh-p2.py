import re


bag_pattern = re.compile(r'^(\w+ \w+)')
carried_pattern = re.compile(r'(\d+) (\w+ \w+)')

# Keys are name of bags, while the values are name of bags that carry the key bag
carrier_dict = {}

with open('input/in7.txt') as f:
    for line in f:
        line = line.rstrip()

        carrier_name = bag_pattern.findall(line)[0]
        carrieds = carried_pattern.finditer(line)

        if carrier_dict.get(carrier_name) is None:
            carrier_dict[carrier_name] = []

        for carried in carrieds:
            count, carried_name = carried.groups()
            count = int(count)
            carrier_dict[carrier_name].append((count, carried_name))

print(carrier_dict)

def find_carried_count(carr_dict, query_name, acc=1):
    carrieds = carr_dict.get(query_name)
    if len(carrieds) == 0:
        return 0
    else:
        deep_counts = sum(c * find_carried_count(carr_dict, q) for c, q in carrieds)
        shallow_counts = sum(c for c, _ in carrieds)
        return deep_counts + shallow_counts

print(find_carried_count(carrier_dict, 'shiny gold'))