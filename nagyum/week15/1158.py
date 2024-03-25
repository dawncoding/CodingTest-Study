"""
N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K가 주어진다.
순서대로 K번째 사람을 제거.
"""

import sys
input=sys.stdin.readline

n,k=map(int,input().split())
people=[i for i in range(1,n+1)]

p_del=[]
i=0

while people:
    i=(i+k-1)%len(people)
    p_del.append(str(people.pop(i)))
print("<",', '.join(p_del),">", sep="") 