"""
Input: 여러 개의 n
Output: 각 n에 대해서, n보다 크고, 2n보다 작거나 같은 소수의 개수
Constraints: 1 <= n <= 123,456

문제 설명
베르트랑 공준: 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다
자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램

문제 풀이
에라토스테네스의 체를 이용해야 한다.
숫자의 제곱근까지만 약수의 여부를 검증하는 함수 isPrime 생성

시간복잡도: 루프 -> O(N)
공간복잡도: num_list 배열의 크기 = N -> O(N)
"""
import sys
input = sys.stdin.readline

# 해당 문제는 123456까지라는 제한된 수가 존재하므로, 123456 * 2 + 1개의 인자가 1인 리스트 생성
num = 123456 * 2 + 1 # 첫번째 리스트는 사용되지 않기 때문에 + 1을 한 것이다.
num_list = [1] * num

for i in range(1, num):
  if i == 1:
    continue
  for j in range(2, int(i ** 0.5) + 1): # 2부터 전달받은 i의 제곱근까지 순회
    if(i % j == 0): # i가 자신의 수 이하의 숫자에 의해 나누어졌을 때 나머지가 0인 경우
      num_list[i] = 0 # 해당 인덱스의 값을 0으로 변경하고, for문 탈출
      break
    # 해당 숫자가 소수인 경우, 해당 인덱스의 리스트 값을 여전히 1이다.
  
while True:
  n = int(input())

  if n == 0:
    break

  prime = 0
  for i in range(n + 1, 2 * n + 1): # n 초과 2n 이하
    prime += num_list[i]
  print(prime)