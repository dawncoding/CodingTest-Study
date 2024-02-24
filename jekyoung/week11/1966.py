from collections import deque
import sys

T = int(input())
    
for _ in range(T):
    N, M = map(int, input().split())
    queue = deque(list(map(int, sys.stdin.readline().split())))
    cnt = 0
    while True:
        maxValue = max(queue)
        front = queue.popleft()
        M -= 1
        if front != maxValue:
            queue.append(front)
            if M < 0:
                M = len(queue) - 1
        else:
            cnt += 1
            if M < 0:
                print(cnt)
                break
    