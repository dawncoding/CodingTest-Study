import sys
input=sys.stdin.readline

bar=list(input())
answer=0
stack=[]

for i in range(len(bar)):
    if bar[i]=="(":
        stack.append("(")
    else:
        if bar[i-1]==")":
            stack.pop()
            answer += 1
        else:
            stack.pop()
            answer += len(stack)