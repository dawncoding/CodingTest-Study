N = int(input())
S = [list(map(int, input().split())) for i in range(N)]
visited = [False]*N
min_diff = float('inf')

def backTracking(depth, index):
    # 조건을 충족시킨다면, 능력치 비교
    global min_diff
    if depth == N//2:
        start, link = 0, 0
        for a in range(N):
            for b in range(N):
                # True는 스타트팀, False는 링크팀
                if visited[a] and visited[b]:
                    start += S[a][b]
                elif not visited[a] and not visited[b]:
                    link += S[a][b]
        # 능력치의 차가 최소인 값을 저장
        min_diff = min(min_diff, abs(start - link))
        return
    
    # 아직 팀원이 채워지지 않았을 때
    for j in range(index, N):
        if not visited[j]:
            visited[j] = True 
            backTracking(depth+1, j+1)
            visited[j] = False  # 방문처리 된 경우에 대해 연산이 끝나고 return 되었다면, 다시 False로 변경

backTracking(0,0)
print(min_diff)