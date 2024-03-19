import sys,heapq
input=sys.stdin.readline
n=int(input())
heap=[]

for i in range(n):
    num=int(input())
    if num:
        heapq.heappush(heap,(abs(num),num))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else
