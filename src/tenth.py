

with open('input/in10.txt') as f:
    lines = f.readlines()
    adapter_joltages = [(i, int(line.rstrip())) for i, line in enumerate(lines)]


device_joltage = max(adapter_joltages, key=lambda x: x[1])[1] + 3
adapter_joltages = sorted(adapter_joltages, key=lambda x: x[1])
jolt_diffs = [3]
current_source_joltage = 0

i = 0
while current_source_joltage != device_joltage - 3:
    joltage_diff = adapter_joltages[i][1] - current_source_joltage
    if 1 <= joltage_diff <= 3:
        jolt_diffs.append(joltage_diff)
        current_source_joltage = adapter_joltages[i][1]
    i += 1


print(jolt_diffs.count(1))
print(jolt_diffs.count(3))
print(jolt_diffs.count(1) * jolt_diffs.count(3))



