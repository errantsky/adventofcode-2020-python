from copy import deepcopy

def iterate(grid):
    """
        (-1, -1)    (-1, 0)     (-1, 1)
        (0, -1)                 (0, 1)
        (1, -1)     (1, 0)      (1, 1)

    :param grid:
    :return:
    """
    to_change = []
    neighbors_d = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    any_change = False
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '.':
                continue

            if grid[i][j] == 'L':
                any_occupied = False
                for dx, dy in neighbors:
                    try:
                        if i + dx < 0 or j + dx < 0:
                            raise IndexError
                        if grid[i + dx][j + dy] == '#':
                            any_occupied = True
                    except IndexError:
                        continue

                if any_occupied is False:
                    any_change = True
                    to_change.append((i, j, '#'))

            elif grid[i][j] == '#':
                count = 0
                for dx, dy in neighbors:
                    try:
                        if i + dx < 0 or j + dy < 0:
                            raise IndexError
                        if grid[i + dx][j + dy] == '#':
                            count += 1
                    except IndexError:
                        continue

                if count >= 4:
                    any_change = True
                    to_change.append((i, j, 'L'))

    for i, j, changed in to_change:
        grid[i][j] = changed

    return any_change, grid


with open('input/in11.txt') as f:
    lines = [list(line.rstrip()) for line in f]

times = 0
while True:
    times += 1
    change_flag, lines = iterate(lines)

    if change_flag is False:
        cnt = 0
        for i in range(len(lines)):
            for j in range(len(lines[0])):
                if lines[i][j] == '#':
                    cnt += 1
        print(cnt)
        break

    # print(f'Result after {times} iterations:')
    # for line in lines:
    #     print(line)


# print(times)