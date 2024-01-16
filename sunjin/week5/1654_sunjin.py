"""
Input: K(오영식이 이미 가지고 있는 랜선의 개수), N(필요한 랜선의 개수) / 랜선의 길이
Output: N개를 만들 수 있는 랜선의 최대의 길이를 센티미터 단위의 정수로 출력
Constraints: 1 <= K <= 10,000 / 1 <= N <= 1,000,000 / K <= N / 1 <= 랜선의 길이 <= 2^31-1

Algorithm: 이분탐색(매개변수 탐색)으로 풀 수 있는 대표적인 알고리즘 문제라고 한다.

시간복잡도: 이분탐색 -> O(NlogM) (N = 랜선의 개수, M: 가장 긴 랜선의 길이)
공간복잡도: list 배열의 크기 = n -> O(N)

1. 최소 길이와 최대 길이의 중간값을 기준으로 주어진 랜선들을 잘랐을 때, 몇 개의 랜선이 나오는지 계산
2. 만약 계산한 랜선의 개수가 필요한 랜선의 개수 n보다 크거나 같다면, mid보다 더 큰 길이로 나눌 수 있는지 탐색 -> start = mid + 1
3. 만약 계산한 랜선의 개수가 필요한 랜선의 개수 n보다 작으면, 더 작은 길이로 나눠야 한다는 뜻 -> end = mid - 1
"""
import sys
input = sys.stdin.readline

k, n = map(int, input().split())
list = [] # 가지고 있는 랜선의 길이를 저장할 리스트

for _ in range(k):
  list.append(int(input()))

start = 1 # 최소 길이
end = max(list) # 랜선 중 가장 긴 길이

while start <= end:
  mid = (start + end) // 2 # 중간값
  lan = 0 # 잘라진 랜선의 개수

  for i in list:
    lan += i // mid # 랜선을 mid의 길이로 잘랐을 때, 잘라진 랜선의 개수

  if lan >= n: # 필요한 랜선의 개수 이상을 만들 수 있는 경우
    start = mid + 1 # mid + 1부터 end까지 탐색
  else: # 필요한 랜선의 개수를 만들 수 없는 경우
    end = mid - 1 # start부터 mid - 1까지 탐색

print(end) # start > end가 될 때, end 값이 가장 긴 랜선의 길이이다.