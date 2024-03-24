import sys

N, r, c = map(int, sys.stdin.readline().split())
result = 0

def div(n):
    global result, r, c
    if n < 0: 
        print(result)
        return
    if 0 <= r < 2**(n-1):
        if 0 <= c < 2**(n-1):
            div(n-1)
        else:           # 2사분면에 해당
            result += 2**(n*2-2)        # 1사분면에 해당하는 만큼의 탐색 횟수 더하기
            c -= 2**(n-1)               # 2^(n-1) 만큼 열을 왼쪽으로 이동시켜 1사분면으로 가정
            div(n-1)
            
    else:
        if 0 <= c < 2**(n-1):   # 3사분면에 해당
            result += (2**(n*2-2))*2    # 1, 2사분면에 해당하는 만큼의 탐색 횟수 더하기
            r -= 2**(n-1)               # 2^(n-1) 만큼 행을 위로 이동시켜 1사분면으로 가정
            div(n-1)
        else:                   # 4사분면에 해당
            result += (2**(n*2-2))*3    # 1, 2, 3사분면에 해당하는 만큼의 탐색 횟수 더하기
            r -= 2**(n-1)               # 2^(n-1) 만큼 행을 위로 이동시켜 1사분면으로 가정
            c -= 2**(n-1)               # 2^(n-1) 만큼 열을 왼쪽으로 이동시켜 1사분면으로 가정
            div(n-1)
    
div(N)