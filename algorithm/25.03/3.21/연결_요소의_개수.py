# 방향이 없는 그래프가 주어졌을 때, 연결요소의 개수를 구하는 프로그램을 작성하시오
# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. 둘째 줄부터 M개의 줄에 간선의 양 끝점u와 v가 주어진다.
# 같은 간선은 한번만 주어진다.

# import sys
# # 제귀 제한 늘려주기
# sys.setrecursionlimit(10000)    # 파이썬에선 재귀 호출 제한이 기본 1000번정도로 설정되어 있음

# DFS함수 정의
def dfs(v):
    visited[v] = True   #현재 노드 방문 표시
    for next_v in graph[v]: # 현재 노드와 연결된 다른 노드들 순회
        if not visited[next_v]: #아직 방문 안 했으면
            dfs(next_v) # 재귀로 계속 방문


N,M = map(int, input().split()) # N: 정점의 개수, M: 간선 개수
graph = [[] for _ in range(N+1)]    #인접 리스트 초기화(1번부터 시작하니까 N+1)

# 간선 정보 입력 받기
for _ in range(M):
    u,v = map(int, input().split()) # 양 끝점 정보
    graph[u].append(v)
    graph[v].append(u)  # 양방향 그래프니까 양쪽 모두 연결

visited = [False] * (N+1)   #방문 여부 표시
count = 0       # 연결 요소 개수 세기

# 모든 노드에 대해 방문 안 했으면 DFS 시작
for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        count += 1   # DFS 한 번 끝날 때마다 연결 요소 하나 추가
print(count)

