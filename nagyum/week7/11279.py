import sys
import heapq
input=sys.stdin.readline

n=int(input())
arr=[]

for i in range (n):
    num=int(input())
    if num ==0:
        try:
            print(-1*heapq.heappop(arr))
        except:
            print(0)
    else:
        heapq.heappush(arr,-num)
        