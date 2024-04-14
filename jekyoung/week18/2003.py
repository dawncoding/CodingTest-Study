import sys

N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

# 투 포인터 알고리즘
s, e = 0, 0
cnt = 0
sum = 0 

while True:
    # 부분합이 M보다 크거나 같은 경우, sum - A[s] & s++
    if sum >= M:
        # M과 같은 경우, cnt++
        if sum == M:
            cnt += 1
        sum -= A[s]
        s += 1
    
    # 부분합이 M보다 작은 경우, sum + A[e] & e++
    else:
        # 끝까지 탐색했다면 종료
        if e == N: break
        sum += A[e]
        e += 1

print(cnt)

'''

def sum(num, idx):
    if idx < N : num += A[idx]
    else: return False
 
    if num == M : 
        return True
    elif num > M :
        return False
    else: return sum(num, idx+1)


for i in range(N):
    result = 0
    if sum(result, i): 
        cnt += 1

print(cnt)
'''