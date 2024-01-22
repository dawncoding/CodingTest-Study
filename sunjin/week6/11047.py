"""
Input: N(준규가 가지고 있는 동전의 종류) / K(가치의 합) / A_i(동전의 가치)
Output: K원을 만드는 데 필요한 동전 개수의 최솟값
Constraints: 1 <= N <= 10 / 1 <= K <= 100,000,000 / 1 <= A_i <= 1,000,000 / A_1 = 1, i>=2인 경우에 A_i는 A_(i-1)의 배수

알고리즘
그리디 알고리즘

시간복잡도: O(NlogN) + O(N) -> O(NlogN)
sort -> O(NlogN)
화폐의 종류 N개 -> O(N)
공간복잡도: a_list의 길이 = N -> O(N)
"""
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
a_list = []
for _ in range(N):
  a = int(input())
  a_list.append(a)

# 내림차순 정렬
a_list.sort(reverse=True)

count = 0
for a in a_list:
  count += K // a
  K %= a

print(count)
