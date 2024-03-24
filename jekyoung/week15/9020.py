import sys

prior = [0]*10001
prior[0], prior[1] = 1, 1
for i in range(2, 5000):
    for j in range(2*i, 10001, i):
        prior[j] = 1


T = int(sys.stdin.readline())
        
for _ in range(T):
    n = int(sys.stdin.readline())
    partition = []
    for i in range(n//2, 0, -1):
        if prior[i] == 0 and prior[n-i] == 0:
            print(i, n-i)
            break
       
    