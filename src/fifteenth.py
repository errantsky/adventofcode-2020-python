
def play(game, turns):
    seen = [0] * turns
    lastnum = game[-1]
    i = 0
    while i < len(game):
        seen[game[i - 1]] = i
        i += 1
    while i < turns:
        j = seen[lastnum]
        seen[lastnum] = i
        lastnum = 0 if j == 0 else i - j
        i += 1
    return lastnum

print(play([15,5,1,4,7,0], 2020))
print(play([15,5,1,4,7,0], 30000000))
