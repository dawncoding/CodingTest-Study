N = int(input())
nums = []
for _ in range(N):
    nums.append(input())

length = len(nums[0])
result = 0
# for l in range(length-1, -1, -1):
#     for i in range(N-1):
#         num_i = nums[i][l:]
#         for j in range(i+1, N):
#             num_j = nums[j][l:]
#             if num_i == num_j:
#                 result = length - l
#                 break
#     if result != length - l: break

# if __ in []: 을 이용하면, for문 2개로 가능.
for l in range(length-1, -1, -1):
    arr = []
    for num in nums:
        if num[l:] in arr: break
        else: arr.append(num[l:])
    if len(arr) == N:
        print(length - l)
        break
 