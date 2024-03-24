N, K = map(int, input().split())

# 사람 번호 부여
arr = [0]*N
for i in range(N):
    arr[i] = i+1

result = []
num=0

for j in range(N):
   num += K-1
   # num이 길이를 초과할 때, 나머지 연산으로 처리
   if num >= len(arr):
       num = num%len(arr)
   result.append(arr.pop(num))

print("<", end="")
for k in range(N):
    if k==N-1: print(result[k], end="")
    else: print(result[k], end=", ")
print(">")