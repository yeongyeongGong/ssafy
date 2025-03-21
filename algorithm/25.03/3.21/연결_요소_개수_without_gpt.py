def dfs(v):
    visited[v] = True
    for i in graph[v]:  # graph의 v와 연결된 요소들을 방문하기기
        if not visited[i]:
            dfs(i)


N, M = map(int, input().split())  # N: 정점의 개수, M: 간선의 개수

graph = [[] for _ in range(N + 1)]  # 그래프 저장
visited = [False] * (N + 1)  # 방문확인 배열
count = 0  # 연결 요소 개수 저장
for _ in range(M):
    u, v = map(int, input().split())  # u,v 양 끝점
    graph[u].append(v)
    graph[v].append(u)  # 양방향 그래프이기 때문에 양쪽 다 append

for i in range(1, N + 1):
    if not visited[i]:  # 방문한적이 없으면 그래프 돌기 시작
        dfs(i)
        count += 1

print(count)
