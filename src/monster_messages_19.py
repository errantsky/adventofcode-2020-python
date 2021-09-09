"""
Day 19: Monster Messages

We have a zero rules to :
    Each rule contains a number of OR conditionals
        Each conditional includes a number of rule numbers, or a single character.

Functions
Given a rule number, rules, and an input, see if rule applies to the input

"""
from typing import List


def match_rule(rule_number: int, mid_inp: List[str], rules):
    rl: List[List[str]] = rules[rule_number]

    for or_cond in rl:
        temp = mid_inp[:]
        # check for single char rule
        if or_cond[0].startswith('"'):
            if temp[0] == or_cond[0][1]:
                temp.pop(0)
                return True, temp
            else:
                return False, None

        # if any of them is true, break and return True
        res = True

        for rnum in or_cond:
            flag, temp = match_rule(int(rnum), temp, rules)
            if not flag:
                res = False
                break
        if res:
            return True, temp

    # if none is true, return False
    return False, None


with open('input/in19.txt') as f:
    lines = [line.rstrip() for line in f.readlines()]
    rules = lines[:lines.index('')]
    rd = dict()
    for rule in rules:
        rule_num = int(rule[:rule.index(':')])
        rule_list = rule[rule.index(' ')+1:].split('|')
        rule_list = [r.split() for r in rule_list]
        rd[rule_num] = rule_list

    rules = rd
    inputs = [list(line) for line in lines[lines.index('')+1:]]

print(inputs)
print(rules)
match_count = 0
for s in inputs:
    r, n = match_rule(0, s, rules)
    if r and len(n) == 0:
        match_count += 1

# assert match_count == 2
print(match_count)

