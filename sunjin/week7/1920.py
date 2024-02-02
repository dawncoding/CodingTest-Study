"""
Input: N / A[1], A[2], ..., A[N] / M
Output: M개의 줄에 답을 출려
Constraints: 1 <= N <= 100,000 / 1 <= M <= 100,000

문제
N개의 정수 A[1], A[2], ..., A[N]이 주어졌을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램

문제 풀이
import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

for i in m_list:
  if i in n_list:
    print(1)
  else:
    print(0)
-> 시간 초과

알고리즘
이분 탐색

시간 복잡도 -> O(NlogN) + O(MllogN) -> O(NlogN)
n_list 정렬 -> O(NlogN) (N: n_list의 길이)
m_list에 M개의 원소가 있으므로, 모든 이분 탐색에 대한 총 시간 복잡도 -> O(MlogN)
공간 복잡도 -> O(N)
n_list, m_list 배열의 길이 -> O(N + M)
"""
import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))
n_list.sort() # O(NlogN)

# m_list의 각 원소별로 이분탐색
for m in m_list:
  left = 0
  right = n-1

  while left <= right:
    mid = (left + right) // 2
    if m > n_list[mid]:
      left = mid + 1
    elif m < n_list[mid]:
      right = mid - 1
    else:
      left = mid
      right = mid
      break
  
  if left == mid and right == mid:
    print(1)
  else:
    print(0)