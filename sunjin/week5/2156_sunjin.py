"""
Input: n(포도주 잔의 개수), 포도주의 양 n개
Output: 최대로 마실 수 있는 포도주의 양
Constraints: 1 <= n <= 10,000 / 0 <= 포도주의 양 <= 1,000

Algorithm: Dynamic Programming

dp[i] = i번째 포도주까지 최대로 마신 포도주의 양
연속으로 놓여 있는 3잔을 모두 마실 수는 없다.

현재 포도주를 마실지 말지를 결정할 때
1. 현재 포도주와 이전 포도주를 마시고 전전 포도주는 마시지 않는다. -> wine[i] + wine[i - 1] + dp[i - 3]
2. 현재 포도주와 전전 포도주를 마시고 이전 포도주는 마시지 않는다. -> wine[i] + dp[i - 2]
3. 현재 포도주를 마시지 않는다. -> dp[i - 1]
"""
import sys
input = sys.stdin.readline

n = int(input())

wine = []
for i in range(n):
    wine.append(int(input()))

dp = [0]*n
dp[0] = wine[0]

if n > 1:
    dp[1] = wine[0] + wine[1]

if n > 2:
    dp[2] = max(wine[2] + wine[1], wine[2] + wine[0], dp[1])

for i in range(3, n):
    dp[i] = max(dp[i - 1], dp[i - 3] + wine[i - 1] + wine[i], dp[i - 2] + wine[i])

print(dp[n - 1])