import re

with open('input/in21.txt') as f:
    lines = [line.strip() for line in f]
    pattern = re.compile(r'^(.*) \(contains (.*)\)$')
    ingredients = [pattern.findall(line)[0][0].split(' ') for line in lines]
    allergens = [pattern.findall(line)[0][1].split(', ') for line in lines]

alg_list = []
for g in ingredients:
    alg_list += g
all_ings = set(ingredients[0])
for i in range(1, len(ingredients)):
    all_ings = all_ings.union(ingredients[i])
all_ing_matches = {}
al_set = set()
for alg in allergens:
    al_set = al_set.union(alg)

red_sets = {}

for allergen in al_set:
    ing_set = set()
    for i, ing in enumerate(ingredients):
        if allergen in allergens[i]:

            if len(ing_set) == 0:
                ing_set = set(ing)

            else:
                ing_set = ing_set.intersection(ing)

    red_sets[allergen] = ing_set

res = []
als = list(al_set)
al_count = len(al_set)
accounted = set()
while True:
    if len(red_sets) == 1:
        k, v = red_sets.popitem()
        v = v.pop()
        res.append((k, v))
        break

    for allergen in als:
        if allergen not in accounted:
            if len(red_sets.get(allergen)) == 1:
                name = red_sets.pop(allergen).pop()
                res.append((allergen, name))
                al_set.remove(allergen)
                accounted.add(allergen)

                for val in red_sets.values():
                    if name in val:
                        val.remove(name)

inal = set([el[1] for el in res])
rr = sorted(res, key=lambda x: x[0])
rr = [r[1] for r in rr]
print(','.join(rr))
res = all_ings.difference(inal)

# for k, v in res:
#     print(f'{k}: {v}')
acc = 0
for k in res:
    acc += alg_list.count(k)

print(acc)