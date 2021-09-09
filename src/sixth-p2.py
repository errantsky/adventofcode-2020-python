

with open('input/in6.txt') as f:
    group_counts = []
    group_all_yes_sets = []

    for line in f:
        line = line.rstrip()

        if line == '':
            acc_set = group_all_yes_sets.pop()
            for s in group_all_yes_sets:
                acc_set = acc_set.intersection(s)

            group_counts.append(len(acc_set))
            group_all_yes_sets = []
        else:
            cur_set = set()
            for yes_answer in line:
                cur_set.add(yes_answer)
            group_all_yes_sets.append(cur_set)

    acc_set = group_all_yes_sets.pop()
    for s in group_all_yes_sets:
        acc_set = acc_set.intersection(s)

    group_counts.append(len(acc_set))

    print(group_counts)
    print(sum(group_counts))