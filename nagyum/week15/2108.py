import sys
from collections import Counter
input=sys.stdin.readline

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

#산술평균
print(round(sum(a)/n))      
#중앙값
print(sorted(a)[len(a)//2]) 

#최빈값
count = Counter(a)           
order = count.most_common()  
max_frequency = order[0][1]  

fq = []                      
for i in order:
    if i[1] == max_frequency: 
        fq.append(i[0])       
        
if len(fq) == 1:           
    print(fq[0])             
else:
    print(sorted(fq)[1])  

#범위
print(max(a)-min(a))



    