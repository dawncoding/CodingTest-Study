import sys
input=sys.stdin.readline

N=int(input())
arr =[int(input()) for _ in range(N)]
tri=[1,1,1,2,2] 

for i in range(5,max(arr)+1):
    tri.append(tri[i-2]+tri[i-3])
    
for i in arr:
    print(tri[i])

