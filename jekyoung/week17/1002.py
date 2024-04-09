import sys

T = int(sys.stdin.readline())

for _ in range (T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    distance = float(((x1-x2)**2 + (y1-y2)**2)**0.5)
    
    # 원의 중심이 동일할 때,
    if distance == 0:
        # 동일한 원
        if r1 == r2: print(-1)
        # 만나지 않는 두 원
        else: print(0)
        continue

    # 원의 중심이 다를 때,
    sum = r1 + r2
    sub = abs(r1-r2)
    if sum == distance or sub == distance:
        # 접하는 경우
        print(1)
    elif sub < distance < sum:
        # 두 점에서 만나는 경우 
        print(2)
    else:
        # 만나지 않는 경우
        print(0)
