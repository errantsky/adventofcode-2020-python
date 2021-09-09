# TODO: find problem lines as you execute instead of accounting for all `jmp` and `nop` lines.

def execute_line(boot_codes, cursor, acc):
    is_bad = False
    line = boot_codes[cursor]

    if line[:3] == 'nop' or line[:3] == 'jmp':
        is_bad = True

    if line[:3] == "nop":
        cursor += 1

    elif line[:3] == "acc":
        sign = line[4]
        value = int(line[5:])
        if sign == "+":
            acc += value
        elif sign == "-":
            acc -= value
        else:
            raise Exception("Bad acc value.")
        cursor += 1

    elif line[:3] == "jmp":
        sign = line[4]
        value = int(line[5:])
        if sign == "+":
            cursor += value
        elif sign == "-":
            cursor -= value
        else:
            raise Exception("Bad acc value.")

    else:
        raise Exception("Bad Op")

    return cursor, acc, is_bad


def repl(bcodes, diag=False):
    executed_lines = set()
    acc = 0
    cursor = 0
    if diag is True:
        plines = []

    while True:
        if cursor >= len(bcodes):
            flag = 200
            print("Program terminated.")
            # print(f'acc: {acc}')
            break
        elif cursor in executed_lines:
            flag = 100
            print(
                f"An instruction is being executed for a second time on line {cursor}:\nacc: {acc}"
            )
            break
        else:
            executed_lines.add(cursor)
            new_cursor, acc, bad_flag = execute_line(bcodes, cursor, acc)
            if diag is True and bad_flag is True:
                plines.append(cursor)
            cursor = new_cursor

    if diag is False:
        return flag, acc
    else:
        return flag, acc, plines

with open("input/in8.txt") as f:
    boot_codes = f.readlines()
    boot_codes = [line.rstrip() for line in boot_codes]


flg, acc, problem_lines = repl(boot_codes, diag=True)

if flg == 100:
    print("Tracing back the faulty line.")
    for line_number in reversed(problem_lines):
        alt_codes = boot_codes.copy()
        faulty_line = alt_codes[line_number]
        if faulty_line[:3] == "jmp":
            alt_codes[line_number] = alt_codes[line_number].replace(faulty_line[:3], "nop")
        elif faulty_line[:3] == "nop":
            alt_codes[line_number] = alt_codes[line_number].replace(faulty_line[:3], "jmp")

        flg, acc = repl(alt_codes)
        if flg == 200:
            print(f"Line {line_number + 1} was faulty.")
            print(f"acc: {acc}")
            break
        else:
            continue
