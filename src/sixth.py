

with open('input/in6.txt') as f:
    group_yes_sets = []
    cur_set = set()
    for line in f:
        line = line.rstrip()
        if line == '':
            # new group
            group_yes_sets.append(cur_set)
            cur_set = set()
        else:
            for answer in line:
                cur_set.add(answer)

    group_yes_sets.append(cur_set)

    print(sum([len(yes_set) for yes_set in group_yes_sets]))
