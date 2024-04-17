import sys

k = int(sys.stdin.readline())
sign = list(sys.stdin.readline().split())

visited = [False]*10
min = []
max = []

def check(i, j, k):
    if k == '<':
        return i < j
    else : 
        return i > j

def solve(depth, s):
    global min, max
    if depth == k+1:
        if len(min)==0:
            min = s.copy()
        else:
            max = s.copy()
        return
    
    for i in range(10):
        if not visited[i]:
            if (depth == 0 or check(s[len(s)-1], i, sign[depth-1])):
                visited[i] = True
                s.append(i)
                solve(depth+1, s)
                s.pop()
                visited[i] = False

solve(0, [])
print(''.join(str(s) for s in max))
print(''.join(str(s) for s in min))