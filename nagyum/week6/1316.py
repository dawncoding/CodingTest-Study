n=int(input())
count=0

for i in range (n):
    word=input()
    for j in range (len(word)-1):
        if word[j] != word[j+1]:
           diff = word[j+1:]
           if word[j] in diff:
               count -= 1
               break
    count +=1
print(count)