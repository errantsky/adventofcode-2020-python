

with open('input/in9.txt') as f:
    numbers = [int(line.rstrip()) for line in f]

preamble_len = 25
window_len = 25

pool = set(numbers[:preamble_len])
earliest_added = numbers[0]
faulty_number = -1

for i in range(preamble_len, len(numbers)):
    found = False
    for num in pool:
        if (numbers[i] - num) in pool:
            found = True
            break
    if not found:
        print(f'{numbers[i]} was not found.')
        faulty_number = numbers[i]
        break

    pool.remove(earliest_added)
    pool.add(numbers[i])
    earliest_added = numbers[i - preamble_len + 1]

for i in range(len(numbers) - 1):
    for j in range(i + 1, len(numbers)):
        contig_sum = sum(numbers[i:j + 1])
        if contig_sum > faulty_number:
            break
        elif contig_sum == faulty_number:
            print(f'Encryption weakness found at ({i}, {j}): {min(numbers[i:j + 1]) + max(numbers[i:j + 1])}')


