import sys
from collections import deque
queue = deque()

def push(x):
    queue.append(x)

def pop():
    if queue:
        front = queue.popleft()
    else:
        front = -1
    print(front)

def size():
    print(len(queue))

def empty():
    if queue:
        print(0)
    else:
        print(1)

def front():
    if queue:
        front = queue.popleft()
        queue.appendleft(front)
    else:
        front = -1
    print(front)

def back():
    if queue:
        back = queue.pop()
        queue.append(back)
    else:
        back = -1
    print(back)


N = int(sys.stdin.readline())
for _ in range (N):
    order = sys.stdin.readline().split()
    if len(order) == 1:
        getattr(sys.modules[__name__], order[0])()
    else:
        func, x = order[0], order[1]
        getattr(sys.modules[__name__], func)(x)
        