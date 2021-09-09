


with open('input/in19-test.txt') as f:
    lines = f.readlines()
    lines = [line.rstrip() for line in lines]


rules = lines[:lines.index('')]
rules = [rule.split(':')[1].strip().split('|') for rule in rules]
rules = [[r.strip().split(' ') for r in rule] for rule in rules]
messages = lines[lines.index('') + 1:]


def match_rule(message, rule, rules):
    global m_ind
    for i in range(len(rule)):
        partial_rule = rule[i]
        if partial_rule[0][0] == '"':
            letter = partial_rule[0].strip('"')
            if message[m_ind] == letter:
                m_ind += 1
                return True
        else:
            for token in partial_rule:
                token_num = int(token)
                if match_rule(message[m_ind:], rules[token_num + 1], rules) is True:
                    continue
                else:
                    if i != len(rule) - 1:
                        
                        continue
                    else:
                        return False
            return True


counter = 0
for message in messages:
    m_ind = 0
    res = match_rule(message, rules[0], rules)
    if res is True:
        counter += 1

print(counter)



