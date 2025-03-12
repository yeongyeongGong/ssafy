T = int(input())  # 테스트 케이스 개수

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 배열 크기 N, 파리채 크기 M
    fly_arr = [list(map(int, input().split())) for _ in range(N)]

    max_fly = 0  # 최대 잡은 파리 개수 초기화

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            sum_fly = 0
            for x in range(M):
                for y in range(M):
                    sum_fly += fly_arr[i + x][j + y]  # 해당 범위 내 모든 파리 개수 합산
            max_fly = max(max_fly, sum_fly)

    print(f"#{tc} {max_fly}")  # 결과 출력
