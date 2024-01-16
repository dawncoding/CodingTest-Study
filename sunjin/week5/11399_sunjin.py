"""
Input: N(사람의 수), P_i(각 사람이 돈을 인출하는 데 걸리는 시간)
Output: 각 사람이 돈을 인출하는 데 필요한 시간의 합의 최솟값
Constraints: 1 <= N <= 1,000 / 1 <= P_i <= 1,000

1. p 정렬
2. p배열 누적합
예) p = [1, 2, 3, 4, 5]
i = index
i = 1일 때, prefixSum[1] = prefixSum[0] + p[1] = 1 + 2 = 3
i = 2일 때, prefixSum[2] = prefixSum[1] + p[2] = 3 + 3 = 6 = 1 + 2 + 3
i = 3일 때, prefixSum[3] = prefixSum[2] + p[3] = 6 + 4 = 10 = 1 + 2 + 3 + 4
3. prefixSum 배열의 요소들의 sum -> 각 사람이 돈을 인출하는 데 필요한 시간의 합의 최솟값

시간 복잡도: O(NlogN) + O(N) = O(NlogN)
공간 복잡도: prefixSum 배열 생성 -> O(N)
"""
import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split(' ')))


p.sort() # 정렬 -> 시간복잡도: O(NlogN)
prefixSum = [0]*n
prefixSum[0] = p[0]
for i in range(1, n): # 루프 -> 시간복잡도: O(N)
  prefixSum[i] = prefixSum[i-1] + p[i]

print(sum(prefixSum))