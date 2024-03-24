import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    # 탐색 범위를 시계방향으로 설정
    dx = [0, -1, -1, -1, 0, 1, 1, 1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]

    # 방문 처리
    arr[y][x] = 0

    for i in range(8):
        nx = x+dx[i]
        ny = y+dy[i]
        # 인덱스 범위 제한
        if 0<=nx<w and 0<=ny<h:
            # 인접한 것이 섬이라면, dfs()
            # bfs를 활용하려면, queue 생성 후 인접한 인덱스 좌표를 추가하여, queue가 비워질 때까지 섬 여부(1) 확인
            if arr[ny][nx] == 1:
                dfs(nx, ny)

while True:
    w, h = map(int, input().split())
    if w==0 and h==0: break
    arr =[]
    result = 0
    for _ in range(h):
        arr.append(list(map(int, sys.stdin.readline().split())))
        
    for i in range(w):
        for j in range(h):
            if arr[j][i] == 1:
                dfs(i, j)
                result += 1
    
    print(result)