import sys

N = int(sys.stdin.readline())

dp = [0]*(N+1)

# 경우의 수 저장 시, 메모리 초과 -> 15746으로 나눈 나머지를 저장
for i in range(1,N+1):
    if i==1 or i==2: dp[i] = i
    else: dp[i] = (dp[i-2] + dp[i-1])%15746

print(dp[N])