import sys
input=sys.stdin.readline

n=int(input())
a=set(map(int, input().split())) #list로 하니까 시간초과가 뜸 왜지
m=int(input())
b=list(map(int,input().split()))

for i in b:
    if i in a:
        print(1)
    else:
        print(0)