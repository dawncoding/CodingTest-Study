word = input()
# 8종류의 알파벳 리스트 생성
croatia = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0

# 'dz='이 word에 포함되는 횟수를 계산
dz_cnt = word.count('dz=')

# croatia 리스트를 돌면서, 동일한 문자가 나타날 때마다 cnt++
for alphabet in croatia:
    cnt += word.count(alphabet)

# 크로아티아 알파벳 갯수: word 길이 - cnt - dz_cnt
print(len(word) - cnt - dz_cnt)