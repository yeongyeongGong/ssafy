T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    # 현재 위치
    r, c = 0, 0

    # 달팽이 숫자의 방향 순서 : 우하좌상
    # dr, dc의 인덱스 의미 >> 0: 우, 1 : 하, 2: 좌, 3: 상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    # 오른쪽으로 이동하면서 N만큼 넣기
    num = 1
    d = 0  # 현재 이동방향

    while True:
        arr[r][c] = num
        num += 1
        if num == N * N + 1:

            pass