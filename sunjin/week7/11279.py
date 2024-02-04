"""
Input: N(연산의 개수) / N개의 줄에 x(연산에 대한 정보) < 2^31
Output: 0이 주어진 횟수만큼 답 출력, 배열이 비어 있는 경우 0 출력
Constraints: 1 <= N <= 100,000

문제
1. 배열에 자연수 x를 넣는다.
2. 배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.
if x == 자연수 -> 배열에 x라는 값을 추가한다.
if x == 0 -> 배열에서 가장 큰 값을 출력하고 그 값을 배열에서 제거한다. 

문제 풀이
heapq는 최소힙으로 구현되어 있기 때문에 최대 힙을 풀기 위해서는 주어진 숫자에 -1을 제곱하여 역순으로 list에 들어갈 수 있도록 하면 된다.

시간 복잡도 -> O(NlogN)
공간 복잡도 -> O(N)
max_heap의 크기 -> O(n)
n, i, num 변수 저장 -> O(1)
"""
import sys, heapq
input = sys.stdin.readline

max_heap = []
n = int(input())
for i in range(n): # 루프 n번 반복 -> O(n)
  num = int(input()) * -1 # 한 번의 입력 및 연산 -> O(1)
  if num == 0: # 비교 연산 -> O(1)
    print(heapq.heappop(max_heap) * -1 if max_heap else 0) # heappop -> 힙에서 원소를 꺼내는 연산 -> 힙의 높이에 따라 O(logn)
  else:
    heapq.heappush(max_heap, num) # 최대 힙에 원소를 추가하는 연산 -> O(logn)
