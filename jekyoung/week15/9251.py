import sys

S1 = list(sys.stdin.readline().strip())
S2 = list(sys.stdin.readline().strip())

# 2차원 배열 생성
dp = [[0 for _ in range(len(S1)+1)] for _ in range(len(S2)+1)]

for i in range(len(S1)):
    for j in range(len(S2)):
        # i, j 번째 알파벳이 같다면, i-1, j-1번째 까지 비교한 LCS에서 + 1
        if S2[j] == S1[i]:
            dp[j+1][i+1] = dp[j][i] + 1
        
        # i, j 번째 알파벳이 다르다면, 'i만 1 증가했을 때'와 'j만 1 증가했을 때'의 LCS 중 최댓값을 선택
        else:
            dp[j+1][i+1] = max(dp[j][i+1], dp[j+1][i])

print(dp[-1][-1])