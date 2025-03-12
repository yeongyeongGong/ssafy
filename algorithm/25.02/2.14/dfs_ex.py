# DFS : 그래프의 모든 정점을 순회하는 방법 중 하나
# 길을 한 방향으로 찾아가다가, 길이 없으면 되돌아가서 다시 탐색하는 방법
# 되돌아갈 수 있도록, 지나온 경로 저장
# 현재위치 : 경로상 마지막 요소 >>> stack에 저장 >>> stack[top], stack[-1]
# start : 시작 정점
# 시작 정점에서부터 방문하는 노드(정점)을 순서대로 '출력'하는 함수
def dfs(start):
    stack = [start] # 시작정점을 넣어서 stack 만들기
    # 방문했던 정점에 재 방문하지 않기 위해서(되돌아가는거 말고) 방문표시
    visited = [0] * (V + 1) # 인덱스가 정점번호, value가 방문 여부 1 또는 0
    visited[start] = 1
    print(start, end= ' ')
    # 현재위치에서 갈 수 있는 길이 있으면 이동하기
    while stack:    #경로상에 길이 있으면 길찾기 계속 해라
        current = stack[-1]
        # current 현재 위치 정점 번호
        # 현재 정점과 연결된 정점을 찾기
        for i in range(1, V + 1):
            # adj[current][i] # current 정점과 i번 정점이 서로 연결되었는가?에대한 정보
            # current와 i가 인접하고, i번 정점에 방문하지 않았으면 방문
            if adj[current][i] and not visited[i] : # adj[current][i] == 1과 똑같은 의미
                stack.append(i)
                visited[i] = 1
                print(i, end=' ')
                break
        else:   # for문을 도는 동안 break가 실행안됨 >>> if 만족안함 >>> 길 없음
            stack.pop() # 현재 위치를 경로에서 제거



# 그래프를 저장할 때는 각 정점들이 어떻게 연결되어 있나를 저장해야 한다.
# edge : 간선, node or vertex : 정점
# 정점의 개수 : V, 간선의 개수 : E
V = 7  # 1~7번까지 있다. (but, 문제에 따라서 0번부터일 수 있으니 잘읽기)
E = 8
# '1 2 1 3 2 4 2 5 3 7 4 6 5 6 6 7'
data = list(map(int, input().split()))
# 그래프를 저장하기 위해서 인접행렬(또는 인접리스트) 활용
adj = [[0] * (V + 1) for _ in range(V + 1)]  # V번 인덱스를 활용하기 위해 V + 1짜리 리스트를 생성

for i in range(0, E * 2, 2):
    # print(data[i], data[i+1])
    a, b = data[i], data[i + 1]
    adj[a][b] = 1
    adj[b][a] = 1
dfs(1)
# for row in adj:
#     print(row)

