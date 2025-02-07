T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    V = list(map(int, input().split()))

    # 🔹 첫 번째 구간의 합을 구함
    min_v = sum(V[:M])
    max_v = sum(V[:M])

    # 🔹 슬라이딩 윈도우 방식으로 구간 합 갱신
    for i in range(N - M + 1):
        sum_v = sum(V[i:i + M])  # i부터 i+M-1까지 슬라이싱으로 합 계산

        if sum_v > max_v:
            max_v = sum_v
        if sum_v < min_v:
            min_v = sum_v

    print(f'#{tc + 1} {max_v - min_v}')
