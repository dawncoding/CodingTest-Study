N = int(input())

for i in range(N):
    word = list(input()) 	#문자를 쪼개서 word 리스트에 저장
    is_group = True 	#문자를 탐색할 때마다 그룹단어 여부는 초기화
    
    for j in range(1, len(word)):
        if word[j] in word[0:j] and word[j] != word[j-1]:
        	#word[0:j]에서 word[j] 동일문자가 있되, 붙어 있지 않다면 그룹단어가 아님
            is_group = False
    
    #그룹단어가 아니므로, N -= 1
    if not is_group: N -= 1
        
print(N)