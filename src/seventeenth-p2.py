from itertools import product

neighborhood = list(product([-1, 0, 1], repeat=4))

grid = set()

with open('input/in17.txt') as f:
    lines = f.readlines()
    lines = [line.rstrip() for line in lines]

n_rows = len(lines)
n_cols = len(lines[0])

for i in range(n_rows):
    for j in range(n_cols):
        if lines[i][j] == '#':
            grid.add((i, j, 0, 0))


def do_cycle():
    changes_todo = []
    # First check which active cubes change
    for x, y, z, w in grid:
        num_active_neighbors = 0
        for dx, dy, dz, dw in neighborhood:
            if (dx, dy, dz, dw) == (0, 0, 0, 0):
                continue

            if (x + dx, y + dy, z + dz, w + dw) in grid:
                num_active_neighbors += 1

        if (2 <= num_active_neighbors <= 3) is False:
            changes_todo.append((False, (x, y, z, w)))

    # Then check inactive cubes that get activated
    for i, j, k, l in grid:
        for di, dj, dk, dl in neighborhood:
                x, y, z, w = i + di, j + dj, k + dk, l + dl
                num_active_neighbors = 0

                for dx, dy, dz, dw in neighborhood:
                    if (dx, dy, dz, dw) == (0, 0, 0):
                        continue

                    if (x + dx, y + dy, z + dz, w + dw) in grid:
                        num_active_neighbors += 1

                if (x, y, z, w) not in grid and num_active_neighbors == 3:
                    changes_todo.append((True, (x, y, z, w)))

    for gets_activated, coords in changes_todo:
        if gets_activated:
            grid.add(coords)
        else:
            grid.remove(coords)


for i in range(6):
    do_cycle()
print(len(grid))