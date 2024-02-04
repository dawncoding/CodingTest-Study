import sys
import heapq as hq

N = int(input())
heap = []

for i in range(N):
    x = int(sys.stdin.readline())
    # x가 자연수인 경우, -x 값을 heappush
    if x>0:
        hq.heappush(heap, -x)
    
    # x가 0인 경우
    else:
    	# heap 리스트가 비어있지 않다면, heappop(heap) 값의 부호를 바꿔 출력
        if heap: print(-hq.heappop(heap))
        # heap 리스트가 비어있다면, 0 출력
        else: print(0)