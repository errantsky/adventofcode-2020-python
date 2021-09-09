
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

def third(slopes):
    with open('input/in3.txt') as f:
        grid = [line.rstrip() for line in f]

    result = 1
    for r, d in slopes:
        row, col = d, r
        num_trees = 0

        while row < len(grid):

            try:
                if grid[row][col % len(grid[0])] == '#':
                    num_trees += 1
            except IndexError:
                print(f'row: {row}, col: {col % len(grid[0])}')

            row += d
            col += r

        result *= num_trees

    return result

print(third(slopes))
    
