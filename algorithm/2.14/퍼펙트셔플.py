# 퍼펙트셔플
# 빈리스트 3개 생성
# 2개는 기존리스트 절반 나눠서 append
# 1개는 셔플할 리스트
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(input().split())
    arr1 = []
    arr2 = []
    shuffle = []
    # arr길이의 절반만큼 반복하면서 각각 리스트에 붙여주기
    for i in range(N // 2):
        arr1.append(arr[i])
        if N % 2 != 0:
            arr2.append(arr[(N // 2) + 1 + i])
        else:
            arr2.append(arr[(N // 2) + i])
    if N % 2 != 0:  # 홀수의 경우에는 arr1에 하나 더 붙여줘야됨
        arr1.append(arr[(N // 2)])

    # 나눈 리스트 두개를 하나의 셔플리스트에 저장
    for i in range(N // 2):
        shuffle.append(arr1[i])
        shuffle.append(arr2[i])
    if N % 2 != 0:  # N이 홀수이면 더많은 요소를 가진 arr1의 마지막 요소를 붙여주기
        shuffle.append(arr1[-1])

    print(f'#{tc}', *shuffle)
