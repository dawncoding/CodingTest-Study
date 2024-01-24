"""
Input: n
Output: 2(세로)*n(가로) 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지
Constraints: 1 <= n <= 1,000

알고리즘
다이나믹 프로그래밍

문제 풀이
n = 1 -> 1가지
n = 2 -> 2가지
n = 3 -> 1 + 2 = 3가지
n = 4 -> 2 + 3 = 5가지
...
dp[1] = 1
dp[2] = 2
i >= 3
dp[i] = dp[i - 1] + dp[i - 2]

시간 복잡도: 루프 반복 -> O(N)
공간 복잡도: dp 배열의 길이 = N -> O(N)
"""
import sys
input = sys.stdin.readline

n = int(input())

dp = [0]*1001
# dp = [0] * (n + 1)을 설정했을 때, 인덱스 에러 발생 -> 이유를 모르겠음

dp[1] = 1
dp[2] = 2
for i in range(3, n+1):
  dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n]%10007)