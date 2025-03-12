T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))

    # data 중에서 최대값과 최소값 차이 찾기
    max_v = 1  # 최대값을 저장할 변수는 가능한 작은 값으로 초기화
    min_v = 1000000  # 최소값을 저장할 변수는 가능한 큰 값으로 초기화
    # 양수인데 엄청 큰값으로 초기화 하고 싶다..
    # min_v = 0xffffffff
    for i in range(N):
        if max_v < data[i]:
            max_v = data[i]
        if min_v > data[i]:
            min_v = data[i]

    # 최대값과 최소값을 구했으니 출력
    print(f'#{tc} {max_v - min_v}')