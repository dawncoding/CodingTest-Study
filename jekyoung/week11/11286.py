import sys
import heapq as hq

N = int(input())

heap = []

'''
# 절대값으로 heap 정렬, 실제 값은 딕셔너리에 key-value 형태로 저장
nums = {}
for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0: 
        if len(heap) == 0: print(0)
        else:
            s = hq.heappop(heap)
            temp = nums[s]
            temp.sort()
            val = temp.pop(0)
            nums[s] = temp
            print(val)
          
    else:
        if abs(x) in nums:
            tp = nums[abs(x)]
            tp.append(x)
            nums[abs(x)] = tp
        else: nums[abs(x)] = [x]
       
        if x > 0: 
            hq.heappush(heap, x)
        else:
            hq.heappush(heap, -x)
'''
        
# heap에 튜플 형태로 저장하면 간단하게 해결 가능
# 튜플에 입력된 값 순서대로 기준을 잡아 정렬됨.
for _ in range(N):
    num = int(sys.stdin.readline())
    if num != 0:
        # 절대값을 기준으로 heap 정렬. 두번째 값으로 실제 값을 넣어줌
        hq.heappush(heap, (abs(num), num))
    else:
        try:
            # 최소의 절대값을 갖는 튜플을 뽑아서, 두번째 값(=실제 값)을 출력
            print(hq.heappop(heap)[1])
        except:
            print(0)
