import sys
input=sys.stdin.readline

n=int(input())
l=sorted(list(map(int,str(n))),reverse=True)

for i in l: 
    print(i,end='')