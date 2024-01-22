"""
Input: none
Output: 10,000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 증가하는 순서로 출력

d(n): 양의 정수 n에 대해서 n과 n의 각 자리 수를 더하는 함수
예) d(75) = 75 + 7 + 5

1 -> 1 + 1 = 2
2 -> 2 + 2 = 4
3 -> 3 + 3 = 6
...
10 -> 10 + 1 + 0 = 11

1. sum에 n 값 추가
2. n의 각 자리 수를 담는 num_list 생성 및 데이터 저장
3. num_list에 있는 수들 sum에 더하기
-> sum = 셀프 넘버 아닌 수
4. data에 있는 sum 제거
-> 1 ~ 4번 과정 계속 반복
-> data에 셀프 넘버인 수만 남게 된다.

시간 복잡도: O(N^2)
공간 복잡도: N개의 수를 담는 data 배열 생성 -> O(N)
"""

data = [] # 1~10000까지의 수를 담는 배열
sum = 0 # d(n) 값을 담는 변수

for i in range(1, 10001): # O(N)
  data.append(i)

for i in range(1, 10001): # 첫번째 루프: O(N), 두번째 루프: O(N) -> O(N^2)
  sum += i
  num_list = list(map(int, str(i)))
  for j in num_list:
    sum += j
  if sum in data:
    data.remove(sum)
  sum = 0

for i in data: # O(N)
  print(i)