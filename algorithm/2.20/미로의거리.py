def bfs(r,c):
    # 2차원 배열이라 출발지는 좌표로 알 수 있다.
    queue = [(r,c, 0)]
    visited = [[0] * N for _ in range(N)]
    visited[r][c] = 1
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    while queue:
        cr, cc, dist = queue.pop(0)
        # 현재 정점과 인접한 정점 찾기
        # 현재 위치에서 갈 수 있는 방향 >>> 상하좌우
        if maze[cr][cc] == 3:
            return dist - 1
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            # 상하좌우에 있으면서 범위안에 있고,
            # 통로(0) 또는 목적지(3), 방문하지 않은 정점
            if 0 <= nr <N and 0<= nc < N:
                if maze[nr][nc] != 1 and not visited[nr][nc]:
                    queue.append((nr, nc, dist + 1))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    # 출발지 찾아서 bfs 수행하면 최단거리를 구할 수 있음

