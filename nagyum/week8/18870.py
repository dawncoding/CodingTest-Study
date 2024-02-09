import sys
input=sys.stdin.readline

N=int(input())
arr=list(map(int,input().split()))

num=sorted(list(set(arr)))
dic=dict(zip(num,list(range(len(num)))))

for x in arr:
    print(dic[x])


