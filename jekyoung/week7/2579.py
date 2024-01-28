N = int(input())
L = [0]*(N+1)

# 계단 별 점수 입력받기
for i in range(1, N+1):
    L[i] = int(input())

if N >= 3:
     dp = [0] * (N+1)
     dp[1] = L[1]
     dp[2] = L[1]+L[2]
     dp[3] = max(L[1]+L[3], L[2]+L[3])

     # 3보다 큰 j번째 계단을 오를 때, 점수의 최댓값은 j-1번째 계단을 밟거나 그렇지 않은 경우로 나뉨
     # 두가지 경우 중 max 값을 dp[j]에 저장
     # 1) j-1번째 계단을 밟는 경우: j-2번째 계단을 밟지 않고 j-3번째 계단을 밟아야 하므로,
     # dp[j-3] + L[j-1] + L[j]
     # 2) j-1번째 계단을 밟지 않는 경우: j-2번째 계단을 밟아야 하므로,
     # dp[j-2] + L[j]
     for j in range(4, N+1):
          dp[j] = max(dp[j-3]+L[j-1]+L[j], dp[j-2]+L[j])

     print(dp[N])

# Index Error 방지
elif N == 2: print(L[1]+L[2])
else: print(L[1])