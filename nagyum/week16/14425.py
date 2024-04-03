import sys
input=sys.stdin.readline

n,m= map(int, input().split())
s= set()

for i in range(n):
    s.add(input())

ans=0

for _ in range(n):
    x=input()
    if x in s:
        ans +=1
print(ans)