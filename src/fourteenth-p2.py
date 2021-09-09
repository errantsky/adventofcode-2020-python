import re
from itertools import product


mem = {}
mem_pattern = re.compile(r"^mem\[(\d+)\] = (\d+)")

with open("input/in14.txt") as f:
    for line in f:
        line = line.rstrip()
        if line[:3] == "mem":
            mem_ind, mem_val = mem_pattern.match(line).groups()
            mem_ind, mem_val = int(mem_ind), list("{:0>36b}".format(int(mem_val)))

            new_addrs = []
            new_ind = list("{:0>36b}".format(mem_ind))
            for i in range(36):
                if mask[i] == "0":
                    continue
                else:
                    new_ind[i] = mask[i]

            float_inds = [i for i in range(36) if new_ind[i] == "X"]
            for inds in product(["0", "1"], repeat=len(float_inds)):
                temp_ind = new_ind[:]
                for i, ind in zip(float_inds, inds):
                    temp_ind[i] = ind

                new_addrs.append(temp_ind)

            for addr in new_addrs:
                iaddr = int("".join(addr), 2)
                mem[iaddr] = mem_val

        elif line[:4] == "mask":
            mask = list(line.split(" = ")[1])

    acc = 0
    for val in mem.values():
        acc += int("".join(val), 2)

print(acc)