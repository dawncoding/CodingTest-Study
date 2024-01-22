"""
Input: N(축구를 하기 위해 모인 사람), S_ij(i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치)
Output: 스타트 팀과 링크 팀의 능력치의 차이의 최솟값
Constraints: 4 <= N <= 20

문제 설명
스타트 팀: N/2명
링크 팀: N/2명
능력치 S_ij: i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치
팀의 능력치: 팀에 속한 모든 쌍의 능력치 S_ij의 합

알고리즘
백트래킹(DFS)
- 스타트와 링크 두 팀으로 나누기 위해 한 팀에 속하면 visited 리스트를 통해 방문 처리를 해주면서 재귀함수 형태로 만든다.
- 만약 한 팀에 속한 팀원의 명수가 n//2로 다 채워졌으면 스타트 팀의 능력치와 링크 팀의 능력치를 구한다.
- 방문 처리된 팀이 스타트 팀이라고 하면, 방문 처리 안된 팀이 링크 팀이다.
- 스타트 팀의 능력치와 링크 팀의 능력치 차이의 절대값과 최소 능력치값을 비교하면서 계속 갱신해준다.

시간 복잡도: 
DFS을 사용하여 모든 가능한 팀 조합 확인 -> O(2^n)
DFS 함수 내부의 이중 for 루프에서 모든 선수 쌍에 대해 능력치를 계산하고 비교하므로 O(n^2)가 추가된다.
-> O(2^n * n^2)
공간 복잡도:
visited 배열의 크기 = n -> O(n)
graph 배열의 크기 = n * n -> O(n^2)
dfs 함수의 재귀 호출 스택에 필요한 공간은 최대 깊이가 n/2인 경우 이므로 -> O(n)
-> O(n^2)
"""
import sys
input = sys.stdin.readline

# n = int(input())

# s = [[0 for _ in range(n)] for _ in range(n)]
# for i in range(n):
#     num_list = list(map(int, input().split()))
#     for j in range(len(num_list)):
#         s[i][j] = num_list[j]

# start = [0 for _ in range(n/2)]
# link = [0 for _ in range(n/2)]

n = int(input())
visited = [False for _ in range(n)] # 1. 1차원으로 방문 리스트 생성
graph = [list(map(int, input().split())) for _ in range(n)]
min_diff = int(1e9) # 2. 최소값을 갱신할 변수 생성

def dfs(depth, idx): # 3. 깊이를 나타내는 변수와 인덱스 변수를 인자로 받아준다.
  global min_diff
  if depth == n // 2: # 4. n은 늘 짝수로 주어진다고 했다. 주어진 수의 절반이 한 팀으로 선택되었을 때 가지치기 시작
    power1, power2 = 0, 0
    for i in range(n):
      for j in range(n):
        if visited[i] and visited[j]: # 5. True의 값을 가지는 팀을 스타트 팀이라고 할 때, 스타트 팀의 능력치를 모두 power1에 더하고
          power1 += graph[i][j]
        elif not visited[i] and not visited[j]: # 6. 나머지 절반 False의 값을 가지는 팀을 링크 팀이라고 할 때, 링크 팀의 능력치를 모두 power2에 더한다.
          power2 += graph[i][j]
    min_diff = min(min_diff, abs(power1 - power2)) # 7. 2중 for문이 끝났을 때, 그 둘의 차이의 절댓값이 변수보다 작으면 변수 갱신
    return

  for i in range(idx, n): # 8. 4번의 조건에 걸리기 전(스타트 팀을 완성하지 못했을 때) 백트래킹 실시
    if not visited[i]:
      visited[i] = True
      dfs(depth + 1, i + 1) # 9. 깊이 +1, 같은 번호 중복을 막기 위한 idx + 1로 재귀 호출
      visited[i] = False

dfs(0,0)
print(min_diff)