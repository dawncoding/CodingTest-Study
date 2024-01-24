n,k=map(int,input().split())
coin=[]
count =0

for i in range(n):
    coin.append(int(input()))
    
coin=sorted(coin,reverse=True)

for i in coin:
    count += k//i
    k %= i
print(count)