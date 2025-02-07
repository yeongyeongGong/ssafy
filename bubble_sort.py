# bubble 정렬
# 1. 두 개씩 비교하면서 큰값을 뒤로 보내기
# 2. 요소의 개수만큼 반복
# [5, 4, 1, 2, 7, 3, 6]
# list: 리스트, array:배열
arr = [5, 4, 1, 2, 7, 3, 6]
N = len(arr)
for j in range(N-1):
    # 0번부터 5번까지 접근
    for i in range(N-1-j):
        # i 번은 i+1번과 비교
        # arr[i], arr[i+1] 중에 큰 숫자를 뒤로 보내기
        # 앞 요소가 더 크면 뒷요소랑 자리 바꾸기
        if arr[i] > arr[i+1]:
            # tmp = arr[i]
            # arr[i] = arr[i+1]
            # arr[i+1] = tmp
            arr[i+1], arr[i] = arr[i], arr[i+1]  # 파이썬에서만 가능한 unpacking

print(arr)