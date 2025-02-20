def bfs(S, G):
    # 거리 계산해야 되니까...거리도 같이 저장
    queue = [(S, 0)]
    visited = [0] * (V + 1)
    visited[S] = 1  # 시작점 방문표시

    while queue:
        front, dist = queue.pop(0)
        if front == G:
            return dist
        for i in range(1, V + 1):
            # g[front][i]==1이면 front와 i가 인접한 정점
            # i에 방문하지 않았으면, 방문
            if g[front][i] and not visited[i]:
                visited[i] = 1
                #이전 정점에서 한 번 더 이동 >> dist + 1
                queue.append((i, dist + 1))

    return 0

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    g = [[0] * (V + 1) for _ in range(V + 1)]
    for _ in range(E):
        a, b = map(int, input().split())
        g[a][b] = 1
        g[b][a] = 1
    S, G = map(int, input().split())
    result = bfs(S,G)
    print(f'#{tc} {result}')
