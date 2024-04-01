import sys
N = int(input())
nums = []
for _ in range(N):
    nums.append(int(sys.stdin.readline()))


def avg():
    print(round(sum(nums)/N))

def mid():
    nums.sort()
    print(nums[N//2])

def freq():
    max_cnt, cnt = 0, 0
    result = []
    temp = nums.copy() + [4001]
    for i in range(N):
        if temp[i] == temp[i+1]:
            cnt += 1
        else:
            if cnt > max_cnt:
                result = [temp[i]]
                max_cnt = cnt
            elif cnt == max_cnt:
                result.append(temp[i])
            cnt = 0

    if not result: print(nums[0])
    elif len(result) == 1: print(result[0])
    else:
        print(result[1])

def rng():
    print(nums[N-1] - nums[0])

avg()
mid()
freq()
rng()