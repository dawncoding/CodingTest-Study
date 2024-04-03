from collections import deque
import sys
input=sys.stdin.readline

n,m=map(int, input().split())
pos=list(map(int,input().split()))
deq=deque([i for i in range(1,n+1)])

cnt=0
for i in pos:
    while True:
        if deq[0]==i:
            deq.popleft()
            break
        else:
            if deq.index(i) <= len(deq)//2:
                deq.rotate(-1)
                cnt += 1
            else:
                deq.rotate(1)
                cnt += 1
                
print(cnt)