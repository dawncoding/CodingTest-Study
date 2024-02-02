"""
Input: stairs(계단의 개수) / score(계단 점수)
Output: 계단 오르기 게임에서 얻을 수 있는 총 점수의 최댓값
Constraints: 1 <= stair <= 300 / 1 <= score <= 10,000

문제
1. 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다.
2. 연속된 세 개의 계단을 모두 밟아서는 안된다.
3. 마지막 도착 계단은 반드시 밟아야 한다.

알고리즘
전형적인 점화식을 찾는 Dynamic Programming 문제, Bottom up 방식
이 문제에서 점화식을 찾을 때 3번 규칙을 따라야 하기 때문에 점화식을 도착지부터 생각하는 방식의 접근이 더 쉽다.

문제 풀이
dp[n] = n번째 계단에 올랐을 때 얻을 수 있는 점수의 최댓값

n번째 계단에 올라오기 위해서는 두 가지 경우가 있다.
1. n-1번째 계단으로 오는 경우
dp[n] = dp[n-3] + stairs[n-1] + stairs[n]
2. n-2번째 계단으로 오는 경우
dp[n] = dp[n-2] + stairs[n]

시간 복잡도 -> O(n) + O(n) -> O(N)
계단의 개수인 n에 대해 for 루프를 통해 stairs 배열을 초기화 -> O(n)
dp 배열 초기화 및 점화식을 이용하여 최댓값을 계산 -> O(n)

공간 복잡도 -> O(N)
stairs 배열의 크기, dp 배열의 크기 -> 선형적으로 증가한다고 가정했을 때, O(N)
"""
import sys
input = sys.stdin.readline

n = int(input())

# 계단의 숫자를 초기화한다. 1층은 1번째(not 0번째) 인덱스에 저장한다.
stairs = [0] * 301
for i in range(1, n + 1):
    stairs[i] = int(input())

# dp 배열을 초기화한다.
dp = [0] * 301
dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]
dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

# 점화식
for i in range(4, n + 1):
    dp[i] = max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i - 2] + stairs[i])

print(dp[n])