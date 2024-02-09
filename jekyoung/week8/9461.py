# dp 리스트 생성
dp = [0]*101
dp[1], dp[2], dp[3], dp[4], dp[5] = 1,1,1,2,2

# 점화식으로 dp 리스트 채우기
for i in range(6, 101):
    dp[i] = dp[i-1]+dp[i-5]

N = int(input())
for _ in range(N):
    idx = int(input())
    print(dp[idx])