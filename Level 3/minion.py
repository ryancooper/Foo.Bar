def answer(minions):
    # your code here
    return sorted(range(len(minions)), key = lambda x : (minions[x][0] * minions[x][2] * 1.0 / minions[x][1], x))