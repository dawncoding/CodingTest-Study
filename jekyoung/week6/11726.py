n = int(input())
# 메모이제이션을 위한 리스트 생성
dp = [0]*1001
dp[1]=1
dp[2]=2

for i in range(3, n+1):
    dp[i] = dp[i-1]+dp[i-2]


print(dp[n]%10007)