import sys
input=sys.stdin.readline

n= int(input())
dp=[0]*301
for i in range(1,n+1):
    dp[i]=int(input())
    
m=[0]*301

m[1]=dp[1]
m[2]=dp[1]+dp[2]
m[3]=max(m[1]+dp[3],dp[2]+dp[3])

for i in range(4,n+1):
    m[i]=max(m[i-2]+dp[i], m[i-3]+dp[i-1]+dp[i])
    
print(m[n])