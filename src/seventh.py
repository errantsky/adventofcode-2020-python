import re


bag_pattern = re.compile(r'^(\w+ \w+)')
carried_pattern = re.compile(r'(\d+) (\w+ \w+)')

# Keys are name of bags, while the values are name of bags that carry the key bag
carried_dict = {}

with open('input/in7.txt') as f:
    for line in f:
        line = line.rstrip()

        carrier_name = bag_pattern.findall(line)[0]
        carrieds = carried_pattern.finditer(line)
        for carried in carrieds:
            count, carried_name = carried.groups()
            if carried_dict.get(carried_name) is None:
                carried_dict[carried_name] = set()
            carried_dict[carried_name].add(carrier_name)
print(carried_dict)

def find_carriers(carr_dict, query_name):
    direct_carriers = carried_dict.get(query_name)
    if direct_carriers is None:
        return {query_name}
    else:
        r = [find_carriers(carr_dict, carrier) for carrier in direct_carriers]
        for rr in r:
            direct_carriers = direct_carriers.union(rr)
        return direct_carriers

res = find_carriers(carried_dict, 'shiny gold')
print(f'count: {len(res)}\n{res}')



