# i 번째 들어갈 요소를 찾아서  i번 요소와 자리 바꿔주기
arr = [6, 5, 1, 2, 4, 8, 2, 7]


def selection_sort(arr):  # 요소를 오름차순 정렬
    N = len(arr)
    # 0번부터 N-1번까지 들어갈 요소 찾아서 바꿔주기
    # i번째에 들어갈 요소를 찾아서 넣어주기
    for i in range(N):  # i : 숫자를 넣는 순서
        # i번째로 작은 숫자 찾기 : 값이 필요한게 아니라 위치!!!
        min_idx = i  # 왜 i번?
        for j in range(i, N):
            # 기존 최소값과 요소를 비교
            if arr[min_idx] > arr[j]:
                min_idx = j
        # 반복문을 완료하면, 최소값의 위치를 찾음
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


selection_sort(arr)
print(arr)
