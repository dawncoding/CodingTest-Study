n=int(input())
time_list=list(map(int,input().split()))

time_list.sort()
a=0

for i in range(1,n+1):
    a += sum(time_list[0:i])
    
print(a)