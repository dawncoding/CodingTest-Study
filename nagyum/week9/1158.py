import sys
input=sys.stdin.readline

n,k=int(input()).split()
arr = [ i for i in range(1,n+1)]

delet = []
num=0

for _  in range(n):
    num += k-1
    if num >= len(arr):
        num=num%len(arr)
        delet.append(str(arr.pop(num)))
        
print("<", ", ".join(delet), ">", sep = '')
        
        