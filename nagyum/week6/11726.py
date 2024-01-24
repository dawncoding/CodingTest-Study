import sys
input = sys.stdin.readline

n=int(input())
dp=[0]*1001 # n+1로 주면 index 에러

dp[1]=1
dp[2] = 2


for i in range(3,n+1):
    dp[i]=(dp[i-1]+dp[i-2])%10007
    
print(dp[n])