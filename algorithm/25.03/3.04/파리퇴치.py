T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())   #N = 배열크기, M = 파리채크기
    fly = []
    max_fly = 0
    for _ in range(N):
        arr = list(map(int, input().split()))
        fly.append(arr)

    for i in range(M):
        for j in range(M):
            
