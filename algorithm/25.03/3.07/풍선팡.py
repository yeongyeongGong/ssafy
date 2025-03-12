T = int(input())    # 테스트케이스
for tc in range(1, T +1):
    N,M = map(int, input().split())
    flower = [list(map(int, input().split())) for _ in range(N)]
    dx = [1,-1,0,0] # 상하좌우
    dy = [0,0,-1,1]
    max_flower = 0
    for x in range(N):   #행
        for y in range(M):  #열
            sum_flower = flower[x][y]
            A = flower[x][y]
            for d in range(4):
                for step in range(1, A + 1):  # 꽃가루 개수만큼 확장
                    nx = x + dx[d] * step
                    ny = y + dy[d] * step
                    if 0 <= nx < N and 0 <= ny < M:
                        sum_flower += flower[nx][ny]

            max_flower = max(max_flower, sum_flower)

    print(f'#{tc} {max_flower}')