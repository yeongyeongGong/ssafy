# 1. 탐색 대상은 정렬된 상태여야 한다.*****
# 2. 탐색 대장의 중간(위치 M)값 과 key를 비교
# 3-1 만약 중간값과 key가 동일하다면 탐색 성공!!!!!
# 3-2 동일하지 않으면 key 가 중간값 보다 큰지 작은지 비교
# 3-3 key가 중간값보다 크다면, 중간보다 작은 영역은 탐색이 불필요
#     탐색범위 : M + 1 ~ end
# 3-4 key가 중간값보다 작다면, 중간보다 큰 영역은 탐색이 불필요
#     탐색범위 : start ~ M-1
# 탐색 범위 변경 뒤 2번부터 반복
arr = [1, 2, 3, 4, 5, 6, 7, 9, 11, 13, 14, 15, 16, 17, 20, 25, 30]


# arr : 탐색 대상
# start : 탐색 시작 인덱스
# end : 탐색 종료 인덱스
# key : 찾고자 하는 값

def binary_search(arr, start, end, key):
    while start <= end:  # start, end의 범위를 재지정하면서 반복
        # 만약 start, end의 값이 역전되면 범위 성립이 안됨 >> 탐색실패
        # if start < end:
        #     break  # 탐색 종료
        mid = (start + end) // 2
        # 중간 값 비교
        if arr[mid] == key:
            return True  # key가 대상 안에 있음!!
        elif arr[mid] > key:  # 중간값은 key가 아니니까 큰지 작은지 비교
            # 중간 값보다 큰 영역은 볼 필요가 없음
            end = mid - 1
            pass
        else:  # arr[mid] < key
            start = mid + 1
            # 반복적으로 값을 찾았지만 key를 찾지 못함
    return False


# 지정한 영역내에 key값이 있으면 True 없으면 False를 반환
def binary_search_recursive(arr, start, end, key):
    if start > end:
        return False
    mid = (start + end) // 2
    if arr[mid] == key:
        return True
    elif arr[mid] > key:  # 중간 이후 영역은 볼 필요가 없음
        binary_search_recursive(arr, start, mid - 1, key)
    else:
        return binary_search_recursive(arr, mid + 1, end, key)


# print(binary_search(arr, 0, len(arr) - 1, 15))
print(binary_search_recursive(arr, 0, len(arr) - 1, 11))
