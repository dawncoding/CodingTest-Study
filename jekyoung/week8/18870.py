import sys

N = int(input())
nums = list(map(int, sys.stdin.readline().split()))
X = list(set(nums))
X.sort()
result = {X[i] : i for i in range(len(X))}

for i in nums:
    print(result[i], end = " ")

# list.index() 사용 시, 시간 초과
# for num in nums:
#     print(X.index(num), end = " ")