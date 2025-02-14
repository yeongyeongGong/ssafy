# start에서 end로 갈 수 있으면 1 아니면 0을 반환하는 함수
def solve(start, end):
    # start에서 dfs해서 end로 갈 수 있는지 확인
    stack = [start]
    visited = [0] * (V + 1)
    visited[start] = 1

    while stack:
        top = stack[-1]
        if top == end:  # 목적지 도착
            return 1
        # 현재 정점과 인접한 정점확인하기
        for i in range(1, V + 1):
            # adj[top][i] == 1 이라면 top과 i가 인접
            if adj[top][i] and not visited[i]:
                stack.append(i)
                visited[i] = 1
                break

        else:
            stack.pop()
    # while문을 수행하는 동안 목적지에 가지 못하면 목적지로 가는길이 없는것 -> 0 반환
    return 0


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adj = [[0] * (V + 1) for _ in range(V + 1)]
    # 그래프 모양 입력받기
    for _ in range(E):
        a, b = map(int, input().split())
        adj[a][b] = 1
    # 시작점과 목적지 입력받기
    start, end = map(int, input().split())
    print(f'#{tc} {solve(start, end)}')