arr=list(range(1,10001)) 
rm_arr=[]

for num in arr:
    for n in str(num):
        num += int(n)
    if num <= 10000:
        rm_arr.append(num)
for rm_num in set(rm_arr):
    arr.remove(rm_num)
for self_num in arr:
    print(self_num)