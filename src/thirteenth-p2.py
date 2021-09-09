

with open('input/in13.txt') as f:
    lines = [line.strip() for line in f]
    earliest_timestamp, bus_ids = lines
    earliest_timestamp = int(earliest_timestamp)
    bus_ids = bus_ids.split(',')
    time_diffs = [i for i in range(len(bus_ids)) if bus_ids[i] != 'x']
    bus_ids = [int(bid) for bid in bus_ids if bid != 'x']



time = 0
increment = 1
for bus, remainder in zip(bus_ids, time_diffs):
    while time % bus != (bus - remainder) % bus:
        time += increment
    increment *= bus

print(time)

