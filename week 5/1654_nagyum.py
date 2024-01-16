K,N=map(int,input().split())
len=[]
for _ in range (K):
    len.append(int(input()))

start=1
end=max(len)

while start <= end:
    mid=(start+end)//2
    line=0
    for i in len:
        line += i//mid
    if line >=N:
        start=mid+1
    else:
        end=mid-1
print(end)