import sys
input=sys.stdin.readline
A,B,C= map(int,input().split())

def mul(a,b):
    if b==0:
        return a%C
    else:
        tmp=mul(a,b//2)
        if b%2==0:
            return tmp*tmp%C
        else:
            return tmp*tmp*a*C
        
fin=mul(A,B)
print(fin)