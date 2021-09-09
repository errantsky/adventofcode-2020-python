# TODO: There is a off by one error with the first algorithm.
def find_boarding_id(boarding_pass):
    row_code = boarding_pass[:7]
    col_code = boarding_pass[7:]

    row = (1, num_rows)
    col = (1, num_cols)

    for bisector in row_code:
        if bisector == 'F':
            row = (row[0], row[0] + (row[1] - row[0]) // 2)
        elif bisector == 'B':
            row = (row[0] + (row[1] - row[0]) // 2 + 1, row[1])

    row = row[0] - 1

    for bisector in col_code:
        if bisector == 'L':
            col = (col[0], col[0] + (col[1] - col[0]) // 2)
        elif bisector == 'R':
            col = (col[0] + (col[1] - col[0]) // 2 + 1, col[1])

    col = col[0] - 1

    boarding_id = row * 8 + col

    # print(f"row: {row}, col: {col}, id: {boarding_id}")
    return boarding_id


num_rows = 128
num_cols = 8
max_id = -1

ids_list = []

with open('input/in5.txt') as f:
    for line in f:
        boarding_id = line.rstrip()
        cur_id = find_boarding_id(boarding_id)
        if cur_id > max_id:
            max_id = cur_id

        ids_list.append(cur_id)

    print(max_id)

ids_list.sort()
print(ids_list)
for i, id_num in enumerate(ids_list):
    if i != len(ids_list) - 1:
        if abs(id_num - ids_list[i + 1]) == 2:
            print(id_num + 1)
            # break

