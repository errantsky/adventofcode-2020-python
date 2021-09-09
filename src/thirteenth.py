

with open('input/in13.txt') as f:
    lines = [line.strip() for line in f]
    earliest_timestamp, bus_ids = lines
    earliest_timestamp = int(earliest_timestamp)
    bus_ids = bus_ids.split(',')
    bus_ids = [int(bid) for bid in bus_ids if bid != 'x']


candidate_timestamp = earliest_timestamp
found = False
while not found:
    for bid in bus_ids:
        if candidate_timestamp % bid == 0:
            found = True
            print(bid * (candidate_timestamp - earliest_timestamp))
            break

    candidate_timestamp += 1
