"""
입력: n
출력: 제곱수 항의 최소 개수
제약: 1 <= n <= 100,000
"""
import sys

input = sys.stdin.readline

n = int(input())

dp = [x for x in range (n+1)]
for i in range(1,n+1):
    for j in range(1,i):
        if j*j > i :
            break
        if dp[i] > dp[i-j*j] + 1 :
            dp[i] = dp[i-j*j] + 1
print(dp[n])