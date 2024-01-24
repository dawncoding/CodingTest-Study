"""
Input: N(단어의 개수), word_list(N개의 단어를 담는 배열)
Output: 그룹 단어의 개수
Constraints: 1 <= N <= 100 / len(word) <= 100

문제 설명
그룹 단어: 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우

문제 풀이
cc a zzz bb -> c a z b (이 형태가 alpha_list에 저장되도록)
kin -> k i n
aa bbb cc b -> a b c b

시간 복잡도: 루프 N번, 루프 word의 길이(M)만큼 반복 -> O(N*M) -> N, M이 선형적으로 증가한다는 가정 하에 -> O(N^2)
공간 복잡도: word_list 배열의 길이 = N, alphabet_list 배열의 길이 = 최대 100 -> 선형적으로 증가한다는 가정 하에 -> O(N)
"""
import sys
input = sys.stdin.readline

word_list = []

# 1. 입력 받기
N = int(input())
for _ in range(N):
  word = input().strip()
  word_list.append(word)

alphabet = ''
# 단어에 나타나는 문자(alpha)를 담는 리스트
alphabet_list = []
# 그룹 단어의 개수
count = 0

# 2. 단어 하나씩 그룹 단어 탐색
for word in word_list: # 루프 N번 -> 시간복잡도: O(N)
  # 2-1. 단어의 각 문자를 탐색
  for j in range(len(word)): # 루프 word의 길이(M)만큼 -> 시간복잡도: O(M)
    # 2-2. 현재 문자가 이전 문자와 다를 경우에만 처리
    if word[j] != alphabet:
      alphabet = word[j]
      alphabet_list.append(alphabet)
  # 2-3. 만약 단어에 있는 문자들이 모두 서로 다른 문자라면, 그룹 단어로 판단하고 count를 증가
  if len(alphabet_list) == len(set(alphabet_list)):
    count += 1
  # 2-4. 초기화
  alphabet = ''
  alphabet_list = []
print(count)