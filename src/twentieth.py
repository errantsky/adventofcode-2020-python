def extract_four_vectors(tile_li):
    vecs = [tile_li[0], tile_li[-1]]
    vr = []
    vl = []
    for i in range(len(tile_li)):
        vr.append(tile_li[i][-1])
        vl.append(tile_li[i][0])
    vecs.append(vr)
    vecs.append(vl)

    return vecs

def and_lists(li1, li2):
    flag = '-1'
    for a, b in zip(li1, li2):
        if a != b:
            flag = '0'
            break

    if flag != '0':
        return 'not-reversed'

    for a, b in zip(reversed(li1), reversed(li2)):
        if a != b:
            return 'false'

    return 'reversed'

with open('input/in20-test.txt') as f:
    lines = f.readlines()
    lines = [line.rstrip() for line in lines]

tile_ids = []
tiles = []
tile = []
for line in lines:
    if line.startswith('Tile'):
        tile_id = line[5:-1]
        tile_ids.append(tile_id)

    elif line == '':
        tiles.append(tile)
        tile = []

    else:
        tile.append(list(line))
tiles.append(tile)

tile_vecs = [extract_four_vectors(tile) for tile in tiles]

sq_sd = {tid: 0 for tid in tile_ids}

for i, tile in enumerate(tile_vecs):
    t_id = tile_ids[i]
    count = 0
    for side in tile:
        for j, other_tile in enumerate(tile_vecs):
            other_id = tile_ids[j]
            other_sides = []
            if i != j:
                for other_side in other_tile:
                    res = and_lists(side, other_side)
                    if res != 'false':
                        count += 1
    sq_sd[t_id] = count



print(sq_sd)


