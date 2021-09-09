from enum import Enum


class Direction(Enum):
    NORTH = (1, 1)
    EAST = (0, 1)
    WEST = (0, -1)
    SOUTH = (1, -1)

dir_dict = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
gl_dict = {'N': (1, 1), 'E': (0, 1), 'S': (1, -1), 'W': (0, -1)}
alt_dict = {0: 'N', 1: 'E', 2: 'S', 3: 'W'}

def rotate_ship(val, current_dir):
    res = (dir_dict[current_dir] + val // 90) % 4
    return alt_dict[res]

with open('input/in12.txt') as f:
    lines = [line.strip() for line in f]
    lines = [(line[0], int(line[1:])) for line in lines]


current_direction = 'E'
current_position = [0, 0]
waypoint = [10, 1]

for direction, amount in lines:
    if direction == 'F':
        current_position[0] += amount * waypoint[0]
        current_position[1] += amount * waypoint[1]

    elif direction == 'E':
        waypoint[Direction.EAST.value[0]] += amount * Direction.EAST.value[1]

    elif direction == 'W':
        waypoint[Direction.WEST.value[0]] += amount * Direction.WEST.value[1]

    elif direction == 'S':
        waypoint[Direction.SOUTH.value[0]] += amount * Direction.SOUTH.value[1]

    elif direction == 'N':
        waypoint[Direction.NORTH.value[0]] += amount * Direction.NORTH.value[1]

    elif direction == 'L':
        current_direction = rotate_ship(amount * -1, current_direction)

    elif direction == 'R':
        current_direction = rotate_ship(amount, current_direction)

    else:
        pass

print(abs(current_position[0]) + abs(current_position[1]))