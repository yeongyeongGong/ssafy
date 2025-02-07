# 테스트 케이스
T = int(input())

# 테스트케이스 T번 반복
for tc in range(1, T + 1):
    # 그림 갯수
    N = int(input())
    # 10 * 10 배열 생성
    arr = [[0] * 10 for _ in range(10)]
    # 보라색 갯수 count
    purple_cnt = 0

    # 그림 갯수만큼 영역 입력받기
    for _ in range(N):
        # a,b,c,d,e => 입력받은 왼쪽 위 모서리, 오른쪽 아래 모서리, 색상정보 리스트
        a, b, c, d, e = map(int, input().split())

        for i in range(b, d + 1):
            for j in range(a, c + 1):
                if e == 1:
                    arr[i][j] += 1
                elif e == 2:
                    arr[i][j] += 2
        print(f'{a}{b}{c}{d}{e}')

        for _ in arr:
            if arr[i][j] == 3:
                purple_cnt += 1

    print(f'#{tc} {purple_cnt}')
