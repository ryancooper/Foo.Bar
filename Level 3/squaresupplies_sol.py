from math import sqrt
def answer(n):
    # your code here
    dp = [0]
    for i in xrange(1, n + 1):
    	dp.append(i)
    	b = int(sqrt(i))
    	for j in xrange(1, b + 1):
    		dp[i] = min(dp[i], dp[i - j * j] + 1)
    return dp[-1]