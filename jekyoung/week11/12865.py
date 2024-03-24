
N, K = map(int, input().split())

dp = [[0 for x in range(K+1)] for y in range(N+1)]

for i in range(1,N+1):
    w, v = map(int, input().split())
    if w <= K :
        for j in range(1, w):
            dp[i][j] = dp[i-1][j]
        for j in range(w, K+1):
            dp[i][j] = max(dp[i-1][j-w]+v, dp[i-1][j])
    else:
        for j in range(1, K+1):
            dp[i][j] = dp[i-1][j]

print(dp[N][K])
