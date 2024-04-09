import sys

N = int(sys.stdin.readline())
P = [0] + list(map(int, sys.stdin.readline().split()))
Max = [0]*(N+1)
Max[1] = P[1]
Max[2] = max(P[2], Max[1]*2)

# Max[i]: 합이 i가 되는 두 수(j, i-j)의 Max[] 합으로 표현 가능
# Max[j]+Max[i-j]의 최댓값이 Max[i]가 된다.
for i in range (3, N+1):
    max_value = P[i]
    for j in range(1, i//2+1):
        max_value = max(max_value, Max[j]+Max[i-j])
    Max[i] = max_value

print(Max[N])