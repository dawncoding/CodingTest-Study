import sys

T = int(sys.stdin.readline())

for _ in range (T):
    x, y = map(int, sys.stdin.readline().split())
    distance = y - x
    tmp = 0     # 이동한 거리
    cnt = 0     # 공간 장치 이동 횟수
    moving = 0  # 반복 횟수 (cnt가 홀수이면 +1되는 특징)

    while tmp < distance:
        cnt += 1
        if cnt % 2 != 0:
            moving += 1
        tmp += moving
    
    print(cnt)