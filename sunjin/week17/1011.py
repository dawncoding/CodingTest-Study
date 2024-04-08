"""
입력: t(테스트 케이스의 개수), x, y
출력: 최소한의 공간이동 장치 작동 횟수
제약: 0 <= x < y < 2^31
"""
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
  x, y = map(int, input().split())
  distance = y - x
  count = 0 # 이동 횟수
  move = 1 # count별 이동 가능한 거리
  move_sum = 0 # 이동한 거리의 합
  while move_sum < distance:
    count += 1
    move_sum += move # count 수에 해당하는 move를 더한다.
    if count % 2 == 0: # count가 2의 배수일 때,
      move += 1
  print(count)