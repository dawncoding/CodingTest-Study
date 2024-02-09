import sys
from collections import deque
input=sys.stdin.readline
deq=deque()
n=int(input()) 
for i in range (n):
    x=input().rstrip().split()
    if (x[0]=="push_front"):
        deq.appendleft(int(x[1]))
    elif (x[0]=="push_back"):
        deq.append(int(x[1]))
    elif (x[0]=="pop_front"):
        if(len(deq)==0):
            print(-1)
        else:
            print(deq.popleft())
    elif (x[0]=="pop_back"):
        if(len(deq)==0):
            print(-1)
        else:
            print(deq.pop())      
    elif(x[0]=="size"):
        print(len(deq)) 
    elif (x[0] == "empty"):
        if (len(deq) == 0):
            print(1)
        else:
            print(0)
    elif (x[0] == "front"):
        if (len(deq) == 0):
            print(-1)
        else:
            print(deq[0])
    elif (x[0] == "back"):
        if (len(deq) == 0):
            print(-1)
        else:
            print(deq[len(deq) - 1])