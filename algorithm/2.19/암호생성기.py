for _ in range(10):
    tc = int(input())  # 테스트 케이스
    arr = list(map(int, input().split()))  # 암호배열

    last = arr[-1]
    i = 1
    while True:  # 배열의 마지막자리가 0이 될 때까지 반복
        first = arr[0] - i  # 맨 앞 원소 저장
        arr = arr[1:] + [first]  # 슬라이싱을 이용하여 맨앞자리 뒤로보내기
        last = arr[-1]

        if last <= 0:
            arr[-1] = 0
            break

        i += 1
        if i > 5:
            i = 1
    print(f'#{tc}', *arr)
