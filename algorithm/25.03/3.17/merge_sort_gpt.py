def merge_sort(arr):
    if len(arr) <= 1:  # 리스트가 한 개거나 비어있으면 정렬 끝
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])  # 왼쪽 반 정렬
    right = merge_sort(arr[mid:])  # 오른쪽 반 정렬

    # 두 정렬된 리스트를 병합
    result = []
    i = j = 0

    while i < len(left) and j < len(right):  # 둘 다 인덱스 범위 안
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 남은 부분 처리
    result += left[i:]
    result += right[j:]

    return result
