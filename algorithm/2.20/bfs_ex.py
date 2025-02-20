'''
7 8
1 2 1 3 2 4 2 5 3 7 4 6 5 6 6 7
'''
# 간선 정보 1 2 1 3 2 4 2 5 3 7 4 6 5 6 6 7
# 정점 개수 :V, 간선의 개수 E
V, E = map(int, input().split())
edges = list(map(int, input().split()))
# 그래프 저장은 인접행렬
adj = [[0] * (V + 1) for _ in range(V + 1)]
for i in range(0, E * 2, 2):
    # edges[i]번 정점과 edges[i+1]번 정점이 연결됨
    # 무향그래프니까 양방향으로 연결되어있다고 표시
    adj[edges[i]][edges[i + 1]] = 1
    adj[edges[i + 1]][edges[i]] = 1


def bfs(start):
    # 시작 정점에서 인접한 정점을 순서대로 방문
    # 방문한 정점에서 다시 인접한 정점을 순서대로 방문
    # 경로를 발견한 순서대로 방문하게 되니까...
    # 방문순서를 queue에 저장하면 된다.
    queue = [start]
    # 정점 재방문을 방지하기 위한 배열
    visited = [0] * (V + 1)
    visited[start] = 1

    # 방문 할 정점이 남아있으면 계속 방문하기
    while queue:
        # 경로를 되돌아오는 개념이 아니라서..바로 pop해야 합니다.
        current = queue.pop(0)
        print(current, end=' ')
        # visited[current] = 1
        # 현재 정점에서 방문가능한 정점을 모두 queue에 담아주기
        # current에서 방문가능한 정점 정보 adj[current]
        for i in range(1, V + 1):
            # adj[current][i] == 1 : current 와 i가 인접한다
            if adj[current][i] == 1 and not visited[i]:
                queue.append(i)
                visited[i] = 1


def bfs2(start):
    # 시작 정점에서 인접한 정점을 순서대로 방문
    # 방문한 정점에서 다시 인접한 정점을 순서대로 방문
    # 경로를 발견한 순서대로 방문하게 되니까...
    # 방문순서를 queue에 저장하면 된다.
    queue = [(start, 0)]
    # 정점 재방문을 방지하기 위한 배열
    visited = [0] * (V + 1)
    visited[start] = 1

    # 방문 할 정점이 남아있으면 계속 방문하기
    while queue:
        # 경로를 되돌아오는 개념이 아니라서..바로 pop해야 합니다.
        current, length = queue.pop(0)
        print(current,length, end=' ')
        # visited[current] = 1
        # 현재 정점에서 방문가능한 정점을 모두 queue에 담아주기
        # current에서 방문가능한 정점 정보 adj[current]
        for i in range(1, V + 1):
            # adj[current][i] == 1 : current 와 i가 인접한다
            if adj[current][i] == 1 and not visited[i]:
                queue.append((i, length + 1))
                visited[i] = 1

def bfs3(start):
    # 시작 정점에서 인접한 정점을 순서대로 방문
    # 방문한 정점에서 다시 인접한 정점을 순서대로 방문
    # 경로를 발견한 순서대로 방문하게 되니까...
    # 방문순서를 queue에 저장하면 된다.
    queue = [start]
    # 정점 재방문을 방지하기 위한 배열
    visited = [-1] * (V + 1)
    visited[start] = 0

    # 방문 할 정점이 남아있으면 계속 방문하기
    while queue:
        # 경로를 되돌아오는 개념이 아니라서..바로 pop해야 합니다.
        current = queue.pop(0)
        print((current,visited[current]), end=' ')
        # visited[current] = 1
        # 현재 정점에서 방문가능한 정점을 모두 queue에 담아주기
        # current에서 방문가능한 정점 정보 adj[current]
        for i in range(1, V + 1):
            # adj[current][i] == 1 : current 와 i가 인접한다
            if adj[current][i] == 1 and visited[i] == -1:
                queue.append(i)
                # 방문체크랑 거리계산 동시에...
                visited[i] = visited[current] + 1


bfs(1)
print('-----------')
bfs2(1)
print('-----------------')
bfs3(1)
