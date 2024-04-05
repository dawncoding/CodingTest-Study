"""
입력: N(명령의 수), N개의 줄에 명령
출력: 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력
제약: 1 <= N <= 2,000,000 (파이썬은 1초에 2000만번 연산 가능)

시간복잡도: 반복문 -> O(N)
공간복잡도: queue 저장 공간 -> O(N)
"""
from collections import deque
import sys

input = sys.stdin.readline

N = int(input().rstrip())
queue = deque()

for _ in range(N):
  text = input().rstrip().split()

  if text[0] == "push":
    data = int(text[1])
    queue.append(data)
  
  elif text[0] == "pop":
    if len(queue) == 0:
      print(-1)
    else:
      print(queue.popleft())
  
  elif text[0] == "size":
    print(len(queue))
  
  elif text[0] == "empty":
    if len(queue) == 0:
      print(1)
    else:
      print(0)
  
  elif text[0] == "front":
    if len(queue) == 0:
      print(-1)
    else:
      print(queue[0])

  elif text[0] == "back":
    if len(queue) == 0:
      print(-1)
    else:
      print(queue[len(queue)-1])