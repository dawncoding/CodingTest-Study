"""
Input: N(인원 수), K(제거하는 사람 순서)
Output: 요세푸스 순열(원에서 사람들이 제거되는 순서)
Constraints: 1 <= K <= N <= 5,000

sol 1)
N, K = map(int, input().split())
arr = [i for i in range(1, N+1)] # 맨 처음에 원에 앉아있는 사람들

answer = [] # 제거된 사람들을 넣을 배열
num = 0 # 제거될 사람의 인덱스 번호

for t in range(N):
  num += K - 1
  if num >= len(arr): # 한 바퀴를 돌고 그 다음으로 돌아올 때를 대비해 값을 나머지로 바꿈
    num = num % len(arr)

  answer.append(str(arr.pop(num)))
print("<",", ".join(answer)[:],">", sep="")

- 시간 복잡도
while 루프 -> O(n)
for 루프 -> O(k-1)
-> 총 연산 횟수 n*(k-1) -> O(n*k) -> O(N)
공간 복잡도: queue, answer의 크기 = n -> O(N)
"""
from collections import deque
n, k = map(int, input().split())
queue = deque(range(1, n + 1))
answer = []

while queue: # queue에 요소가 남아있는 동안 계속된다. O(n)
    for _ in range(k-1): # O(k-1)
        queue.append(queue.popleft())
    answer.append(queue.popleft())
# 총 연산 횟수 n*(k-1) -> O(n*k) -> O(N)

print(str(answer).replace('[', '<').replace(']', '>'))