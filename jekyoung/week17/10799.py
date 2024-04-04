import sys

irons_input = list(sys.stdin.readline().strip())
irons = []
i=0

# () 레이저를 'R'로 치환
while i < len(irons_input):
    if irons_input[i] == '(' and irons_input[i+1] == ')':
        irons.append('R')
        i += 2
    else:
        irons.append(irons_input[i])
        i += 1

# 영향을 미치지 않는 R 제거
temp = ''.join(irons).lstrip('R').rstrip('R')
irons = list(temp)
        
nums = 0    # R의 영향을 받는 막대기의 수
result = 0
for i in range(len(irons)):
    if irons[i] == '(':     # R의 영향을 받는 막대기가 추가된 것
        nums += 1
    elif irons[i] == 'R':   # R의 영향을 받는 막대기 수만큼 잘림
        result += nums
    else:                   # ')'는 막대기가 끝남을 의미하므로,
        nums -= 1           # 영향 받는 막대기 수 -1, 
        result += 1         # R이 없어도 하나의 막대기 조각이 발생

print(result)