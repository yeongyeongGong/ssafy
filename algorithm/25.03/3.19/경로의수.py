# 인접행렬 + 재귀 ver
# v: 현재 정점 번호
# v번에서 갈 수 있는 경로로 모두 이동해보기
# dfs 재귀로 구현하기
# v : 현재 정점 번호
# v번에서 갈 수 있는 경로로 모두 이동해보기
def dfs(v):
    global path_cnt
    if visited[v] == 1:
        return
    if v == G:
        path_cnt += 1
        return
    visited[v] = 1
    # v번 노드에서 갈 수 있는 경로 >>> v번과 인접한 정점 찾기
    # g[v] << v번 정점과 인접한 정점 정보
    for i in range(1, N + 1):
        if g[v][i] == 1:  # v번에서 i번 정점으로 이동가능..
            dfs(i)
    visited[v] = 0  # 방문 표시 지워주기


T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())
    # 정점번호는 1번부터 N번까지
    g = [[0] * (N + 1) for _ in range(N + 1)]
    edges = list(map(int, input().split()))
    for i in range(0, E * 2, 2):
        # 방향그래프이기 때문에 단방향만 정의
        # edges[i], edges[i+1]
        g[edges[i]][edges[i + 1]] = 1
    S, G = map(int, input().split())
    path_cnt = 0
    visited = [0] * (N + 1)
    dfs(S)
    print(f'#{tc} {path_cnt}')
