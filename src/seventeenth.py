# TODO Support variable dimensions and streamline the for loop
from itertools import product


neighborhood = list(product([-1, 0, 1], repeat=3))

grid = set()

with open('input/in17.txt') as f:
    lines = f.readlines()
    lines = [line.rstrip() for line in lines]

n_rows = len(lines)
n_cols = len(lines[0])

for i in range(n_rows):
    for j in range(n_cols):
        if lines[i][j] == '#':
            grid.add((i, j, 0))


def do_cycle():
    changes_todo = []
    # First check which active cubes change
    for x, y, z in grid:
        num_active_neighbors = 0
        for dx, dy, dz in neighborhood:
            if (dx, dy, dz) == (0, 0, 0):
                continue

            if (x + dx, y + dy, z + dz) in grid:
                num_active_neighbors += 1

        if (2 <= num_active_neighbors <= 3) is False:
            changes_todo.append((False, (x, y, z)))

    # Then check inactive cubes that get activated
    for i, j, k in grid:
        for di, dj, dk in neighborhood:
                x, y, z = i + di, j + dj, k + dk
                num_active_neighbors = 0

                for dx, dy, dz in neighborhood:
                    if (dx, dy, dz) == (0, 0, 0):
                        continue

                    if (x + dx, y + dy, z + dz) in grid:
                        num_active_neighbors += 1

                if (x, y, z) not in grid and num_active_neighbors == 3:
                    changes_todo.append((True, (x, y, z)))

    for gets_activated, coords in changes_todo:
        if gets_activated:
            grid.add(coords)
        else:
            grid.remove(coords)


for i in range(6):
    do_cycle()
print(len(grid))