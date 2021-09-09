import re


mem = {}
mem_pattern = re.compile(r'^mem\[(\d+)\] = (\d+)')

with open('input/in14.txt') as f:
    for line in f:
        line = line.rstrip()
        if line[:3] == 'mem':
            mem_ind, mem_val = mem_pattern.match(line).groups()
            mem_ind, mem_val = int(mem_ind), list("{:0>36b}".format(int(mem_val)))

            for i in range(36):
                mask_token = mask[i]
                if mask_token == 'X':
                    continue
                else:
                    mem_val[i] = mask[i]

            mem[mem_ind] = mem_val

        elif line[:4] == 'mask':
            mask = list(line.split(' = ')[1])


    acc = 0
    for val in mem.values():
        acc += int(''.join(val), 2)

print(acc)
