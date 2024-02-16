import sys
input=sys.stdin.readline
"""
N=int(input())
arr =[int(input()) for _ in range(N)]
tri=[1,1,1,2,2] 

for i in range(5,max(arr)+1):
    tri.append(tri[i-2]+tri[i-3])
    
for i in arr:
    print(tri[i])

"""

N=int(input())
dp=[0]*100
dp[0],dp[1],dp[2],dp[3],dp[4]=1,1,1,2,2

for i in range(5,100):
    dp[i] = dp[i-2]+dp[i-3]
    
for _ in range(N):
    i=int(input())
    print(dp[i])