"""
Input: T(테스트 케이스의 개수), N
Output: 각 테스트 케이스마다 0이 출력되는 횟수, 1이 출력되는 횟수
Constraints: N은 자연수 or 0, N <= 40

import sys
input = sys.stdin.readline

def fibonacci(n):
  global countZero, countOne
  if (n == 0):
    countZero += 1
    return 0
  elif (n == 1):
    countOne += 1
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)

t = int(input())

for i in range(t):
  n = int(input())
  countZero = 0
  countOne = 0
  fibonacci(n)
  print(countZero, countOne)
-> 시간 초과

피보나치 수열 f(n) = f(n - 1) + f(n - 2)
n = 0 -> countZero = 1, countOne = 0
n = 1 -> countZero = 0, countOne = 1
n = 2 -> countZero = 1, countOne = 1
n = 3 -> countZero = 1, countOne = 2
n = 4 -> countZero = 2, countOne = 3
n = 5 -> countZero = 3, countOne = 5
n = 6 -> countZero = 5, countOne = 8
n = 7 -> countZero = 8, countOne = 13
dp[n] = [dp[n-1][0] + dp[n-2][0], dp[n-1]dp[1] + dp[n-2][1]]

시간복잡도: O(t * n)
공간복잡도: dp배열의 크기 = n + 1 -> O(n)
"""
import sys
input = sys.stdin.readline

t = int(input())

for i in range(t): # O(t)
  n = int(input())
  dp = [[0, 0] for _ in range(n + 1)]
  dp[0] = [1, 0]
  dp[1] = [0, 1]

  for i in range(2, n+1): # O(n)
    dp[i] = [dp[i-1][0]+dp[i-2][0], dp[i-1][1]+dp[i-2][1]]

  print(dp[n][0], dp[n][1])
  