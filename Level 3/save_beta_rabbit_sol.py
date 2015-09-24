def answer(food, grid):
	# your code here
	N = len(grid)
	dp = [[[0 for k in xrange(food + 1)] for i in xrange(N)] for j in xrange(N)]
	for k in xrange(0, food + 1):
		dp[N - 1][N - 1][k] = -1 if k < grid[N - 1][N - 1] else grid[N - 1][N - 1]
	for j in reversed(xrange(N - 1)):
		for k in xrange(0, food + 1):
			dp[N - 1][j][k] = -1 if k < grid[N - 1][j] else (-1 if dp[N - 1][j + 1][k - grid[N - 1][j]] == -1 else dp[N - 1][j + 1][k - grid[N - 1][j]] + grid[N - 1][j])
	for i in reversed(xrange(N - 1)):
		for k in xrange(0, food + 1):
			dp[i][N - 1][k] = -1 if k < grid[i][N - 1] else (-1 if dp[i + 1][N - 1][k - grid[i][N - 1]] == -1 else dp[i + 1][N - 1][k - grid[i][N - 1]] + grid[i][N - 1])
	for i in reversed(xrange(N - 1)):
		for j in reversed(xrange(N - 1)):
			for k in xrange(0, food + 1):
				if k < grid[i][j]:
					dp[i][j][k] = -1
				else:
					dp[i][j][k] = max(-1 if dp[i][j + 1][k - grid[i][j]] == -1 else dp[i][j + 1][k - grid[i][j]] + grid[i][j], -1 if dp[i + 1][j][k - grid[i][j]] == -1 else dp[i + 1][j][k - grid[i][j]] + grid[i][j])
	res = max(dp[0][0])
	return -1 if res == -1 else food - res