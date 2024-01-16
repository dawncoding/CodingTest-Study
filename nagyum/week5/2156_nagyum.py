n=int(input())
arr=[0]*10000 #각 포도주의 양
for i in range(n):
    arr [i]=int(input())
    
drink=[0]*10000 #최대로 마실 수 있는 포도주의 양
drink[0]=arr[0] # 첫번째 잔의 양이 최대
drink[1]=arr[0]+arr[1] #두번째까지 마신 양이 최대 양
drink[2]=max(arr[2]+arr[1],arr[2]+arr[0],drink[1])
#세잔을 연속으로 마실 수 없다고 했으니까 나올 수 있는 세가지 경우의 수 중에 최대

for i in range (3,n): 
    drink[i]=max(arr[i]+arr[i-1]+drink[i-3],arr[i]+drink[i-2],drink[i-1])
#i번째 포도주를 안 마실 때: drink[i-1]는 이전상태에서의 최대양
#i번째 포도주를 마실고 i-1은 안 마실 때 : arr[i]+drink[i-2]는 현재 포도주와 i-2번째까지의 최대
#i번째 포도주를 마시고 i-1번째 포도주도 마실 때 : arr[i]+arr[i-1]과 세잔 연속은 안되니 i-3번째까지 마셨을 때 최대값
print(max(drink))