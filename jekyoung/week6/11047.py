N, K = map(int, input().split())
coins = []
cnt = 0

# 입력받은 동전 가치를 리스트에 저장
for i in range(N):
    coins.append(int(input()))

# 가장 큰 가치의 동전부터 사용한다.
for j in range(N-1, -1, -1):
    # 남아있는 금액보다 동전의 가치가 작거나 같을 때, 지불 가능
    if K >= coins[j]:
        cnt += K//coins[j]
        K = K%coins[j]

print(cnt)