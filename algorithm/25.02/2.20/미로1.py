# 목적지에 도달할 수 있으면 1 못하면 0 반환
def bfs(sr, sc):
    queue = [(sr, sc)]  # 방문할 정점을 저장하는 queue

    visited = [[0] * 16 for _ in range(16)]
    visited[sr][sc] = 1  # 시작점 재방문 방지
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    while queue:  # 방문할 정점이 남아있으면
        cr, cc = queue.pop(0)

        # 현재 정점과 인접한 정점 둘러보기>> 상하좌우
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            # 벽으로 둘러져 있기 때문에 범위검사는 할 필요가 없음
            # 통로이면서, 방문하지 않았으면 방문하기
            if maze[nr][nc] == 0 and not visited[nr][nc]:
                queue.append((nr,nc))
                visited[nr][nc] = 1
            elif maze[nr][nc] == 3:
                return 1
    # while문이끝남 >>> 방문할 수 있는 정점을 다 방문했음
    return 0

T = 10
for _ in range(T):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    # 출발지 찾기
    is_find = 0
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                is_find = bfs(i, j)
                break
    print(f'#{tc} {is_find}')
