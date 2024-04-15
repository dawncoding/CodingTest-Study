from collections import deque


# 회전시킬 톱니바퀴 번호
# 회전 방향
# 극이 다르면 반대방향, 같으면 회전X

wheel_1 = list(input())
wheel_2 = list(input())
wheel_3 = list(input())
wheel_4 = list(input())

K = int(input())

def roll(nth, wheel, dir, is_first):
    if not nth:
        if is_first: changed_dir = dir
        else: changed_dir = (-1)*dir
        if changed_dir == 1:
            tail = wheel.pop()
            return [tail] + wheel, changed_dir
        elif changed_dir == 0:
            return wheel, 0
        else:
            head = wheel.pop(0)
            return wheel + [head], changed_dir
    else:
        return wheel, 0

    

for _ in range(K):
    num, direction = map(int, input().split())
    
    if wheel_1[2] == wheel_2[6]: first = True
    else: first = False

    if wheel_2[2] == wheel_3[6]: second = True
    else: second = False

    if wheel_3[2] == wheel_4[6]: third = True
    else: third = False

    if num == 1:
        wheel_1, dir = roll(False, wheel_1, direction, True)
        wheel_2, dir = roll(first, wheel_2, direction, False)
        wheel_3, dir = roll(second, wheel_3, dir, False)
        wheel_4, dir = roll(third, wheel_4, dir, False)
    elif num == 2:
        wheel_2, dir = roll(False, wheel_2, direction, True)
        wheel_1, dir = roll(first, wheel_1, direction, False)
        wheel_3, dir = roll(second, wheel_3, direction, False)
        wheel_4, dir = roll(third, wheel_4, dir, False)
    elif num == 3 :
        wheel_3, dir = roll(False, wheel_3, direction, True)
        wheel_4, dir = roll(third, wheel_4, direction, False)
        wheel_2, dir = roll(second, wheel_2, direction, False)
        wheel_1, dir = roll(first, wheel_1, dir, False)
    else:
        wheel_4, dir = roll(False, wheel_4, direction, True)
        wheel_3, dir = roll(third, wheel_3, direction, False)
        wheel_2, dir = roll(second, wheel_2, dir, False)
        wheel_1, dir = roll(first, wheel_1, dir, False)


print(int(wheel_1[0])+2*int((wheel_2[0]))+4*int((wheel_3[0]))+8*int((wheel_4[0])))