"""
입력: n, m / a[1], a[2], ..., a[N]
출력: 경우의 수
제약: 1 <= n <= 10,000 / 1 <= m <= 300,000,000 / 1 <= a[x] <= 30,000
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

left, right = 0, 1
count = 0

while right <= n and left <= right:
  sum_nums = a[left:right]
  total = sum(sum_nums)

  if total == m:
    count += 1

    right += 1
  
  elif total < m:
    right += 1

  else:
    left += 1

print(count)