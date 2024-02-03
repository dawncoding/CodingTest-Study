import sys

N=int(input())
deque=[]

def push_front(x):
    global deque
    deque = [x]+deque
def push_back(x):
    global deque
    deque.append(x)
def pop_front():
    global deque
    if len(deque) == 0: print(-1)
    else:
        print(deque[0]) 
        deque = deque[1:len(deque)]
def pop_back():
    global deque
    if len(deque) == 0 : print(-1)
    else:
        print(deque[len(deque)-1]) 
        deque.pop()
def size(): 
    global deque
    print(len(deque))
def empty():
    global deque
    if len(deque) == 0 : print(1)
    else: print(0)
def front():
    global deque
    if len(deque) == 0: print(-1)
    else: print(deque[0])
def back():
    global deque
    if len(deque) == 0: print(-1)
    else: print(deque[len(deque)-1])

for _ in range (N):
    order = sys.stdin.readline().split()
    if len(order) == 1:
        order = order[0]
        locals()[order]()

    else:
        order, x = order[0], order[1]
        locals()[order](x)
