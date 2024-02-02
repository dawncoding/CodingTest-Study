N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

# A 리스트 오름차순 정렬
A.sort()

# 이진 탐색을 위한 재귀함수 생성
def binarySearch(target, start, end):
     mid = (start+end)//2
     if start>end: print(0)		# 탐색을 모두 마쳤는데 동일한 값이 없는 경우 0출력
     # target이 A[mid]보다 작다면 end = mid-1 으로 하여 다시 탐색
     elif target < A[mid]: binarySearch(target, start, mid-1)
     # target이 A[mid]보다 크다면 start = mid+1 으로 하여 다시 탐색
     elif target > A[mid]: binarySearch(target, mid+1, end)
     else: print(1)		# target == A[mid]인 경우 1 출력

for num in B:
     binarySearch(num, 0, N-1)
