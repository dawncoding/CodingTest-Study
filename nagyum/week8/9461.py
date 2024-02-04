import sys
input=sys.stdin.readline

N=int(input())
tri=[1,1,1,2,2] 

for i in range(5,99):
    tri.append(tri[i-2]+tri[i-3])
    
for _ in range(N):
    x=int(input())
    print(tri[x])


