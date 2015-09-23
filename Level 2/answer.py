def answer(names):
    # your code here
    getScore = lambda str : reduce(lambda acc, x : acc + ord(x) - ord('a') + 1, str, 0)
    return sorted(names, key = lambda name : (getScore(name), name), reverse = True)