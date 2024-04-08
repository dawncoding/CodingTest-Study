"""
입력: N(구매하는 카드 개수)
출력: 지불해야 하는 금액의 최댓값
제약: 1 <= N <= 1,000 / 1 <= P_i <= 10,000

4
3 5 15 16
dp[1] = 3
dp[2] = dp[1] + p[1] 또는 p[2] 둘 중 큰 값 = 8
dp[3] = dp[1] + p[2] 또는 dp[2] + p[1], p[3] 중 큰 값 = 15
dp[4] = dp[1] + p[3], dp[2] + p[2], dp[3] + p[1], p[4] 중 큰 값 = 18

점화식 dp[i] = dp[i-j] + p[j]
"""

import sys

input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))
p.insert(0,0)
dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
  for j in range(1, i+1):
    dp[i] = max(dp[i], p[j] + dp[i-j])
print(dp[n])