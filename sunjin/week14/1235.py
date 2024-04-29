"""
학생들의 번호가 주어졌을 때, 뒤에서 k자리만을 추려서 남겨놓았을 때 모든 학생들의 학생 번호를 서로 다르게 만들 수 있는 최소의 k

입력: n(학생 수), string num(n개의 학생 번호)
출력: k
제약: 2 <= n <= 1,000 / len(num) <= 100
"""
import sys

input = sys.stdin.readline

# 입력
n = int(input())

num_list = []
for _ in range(n):
  num = input().rstrip()
  num_list.append(num)


end = len(num_list[0])

j = 1
k = 1
loop = "continue"
sol_list = []
sol_set = {}

while loop == "continue":
  for i in range(n):
    sol_list.append(num_list[i][end-j:end])
    sol_set = set(sol_list)
  if len(sol_list) == len(sol_set):
    loop = "end"
    break
  j += 1
  k += 1
  sol_list.clear()
  sol_set.clear()

print(k)