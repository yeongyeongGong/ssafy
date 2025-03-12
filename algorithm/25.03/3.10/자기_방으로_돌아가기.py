T = int(input())  # 테스트케이스

for tc in range(1, T + 1):
    N = int(input())  # 돌아가야할 학생 수
    corridor = [0] * 201    # 복도
    for i in range(N):
        s, e = map(int, input().split())  # s : 현재 위치, e: 이동해야할 방 위치

        s = (s + 1) // 2
        e = (e + 1) // 2

        if s > e:
            for i in range(e, s+1):
                corridor[i] += 1
        elif s < e:
            for i in range(s, e + 1):
                corridor[i] += 1

    print(f'#{tc} {max(corridor)}')
