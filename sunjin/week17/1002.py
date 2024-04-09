"""
입력: T(테스트 케이스의 개수), x_1, y_1, r_1, x_2, y_2, r_2
출력: 각 테스트 케이스마다 류재명이 있을 수 있는 위치의 수
제약: -10,000 <= x_1, y_1, x_2, y_2 <= 10,000 / 1 <= r_1, r_2 <= 10,000
"""
from math import sqrt
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
  x1, y1, r1, x2, y2, r2 = map(int, input().split())
  distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

  # 조규현과 백승환의 위치가 동일할 때 = 원의 중심이 일치할 때
  if (distance == 0):
    # 반지름도 동일하면 무한히 많은 점에서 만난다.
    if r1 == r2:
      print(-1)
    # 반지름이 다르면 만나지 않는다.
    else:
      print(0)

  # 조규현화 백승환의 위치가 다를 때 = 두 원의 중심이 다른 경우 -> distance != 0
  else:
    """
    틀린 조건

    # 큰 원 안에 작은 원이 내접하지 않은 상태로 안에 있을 때 or 두 원이 겹치지 않았을 때
    if (r2 > r1 + distance or distance > r1 + r2): -> distance > r1 + r2 조건으로 작은 원이 큰 원 안에 있는 경우를 고려하지 못한다.
      print(0)
    # 두 원이 내접할 때 or 외접했을 때
    elif (r2 == r1 + distance or distance == r1 + r2):
      print(1)
    # 두 원이 겹쳤을 때
    elif (distance < r1 + r2 and distance > abs(r1 - r2)):
      print(2)
    """
    # 두 원의 중심이 다른 경우

    # 두 원의 중심 거리가 두 반지름의 합보다 클 경우
    if distance > r1 + r2:
        print(0)
    # 한 원이 다른 원 내부에 있으며 내접하지 않을 경우
    elif distance < abs(r1 - r2):
        print(0)
    # 두 원이 외접할 경우
    elif distance == r1 + r2:
        print(1)
    # 한 원이 다른 원 내부에 있으며 내접할 경우
    elif distance == abs(r1 - r2):
        print(1)
    # 두 원이 두 점에서 교차할 경우
    elif abs(r1 - r2) < distance < r1 + r2:
        print(2)