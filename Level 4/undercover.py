from math import factorial

def memo(func):
    cache = {}
    def newFunc(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return newFunc

@memo
def C(N, K):
    return factorial(N) / (factorial(K) * factorial(N - K)) if N >= K else 0

@memo
def T(N, K):
    # total number graph formed by n vertices with k edges
    return C(N * (N - 1) / 2, K)

@memo
def D(N, K):
    # total number disconnected graph formed by n vertices with k edges
    # that means a vertex v is in a connected graph with i < N nodes
    # and with j edges (i - 1 <= j <= min{K, T(i, 2)})
    res = 0
    for i in xrange(1, N):
        for j in xrange(i - 1, min(K, i * (i - 1) / 2) + 1):
            res += C(N - 1, i - 1) * S(i, j) * T(N - i, K - j)
    return res

@memo
def S(N, K):
    # total number of connected labeled graph formed by n vertices with k edges
    if N <= 1:
        return 1
    return T(N, K) - D(N, K) if K > N - 1 else N ** (N - 2)

def answer(N, K):
    # your code here
    return str(S(N, K))
    