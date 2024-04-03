import sys
input=sys.stdin.readline

n=int(input())
p=[list(map(int,input().split())) for _ in range(n)]

blue=0
white=0

def solution(x,y,n):
    global blue, white
    color=p[x][y]
    d=n//2
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color != p[i][j]:
                solution(x,y,d)
                solution(x,y+d,d)
                solution(x+d,y,d)
                solution(x+d,y+d,d)
                return
    if color==0:
        white += 1
    else:
        blue += 1
        
solution (0,0,n)
print(white)
print(blue)