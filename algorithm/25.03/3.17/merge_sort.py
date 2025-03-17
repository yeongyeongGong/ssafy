# 병합정렬 : 전체를 정렬하기 위해서
# 정렬된 두 개를 합치는 알고리즘
arr = [8, 5, 1, 2, 9, 10, 4, 7, 3, 6]
N = len(arr)


# 리스트를 인자로 받아서, 정렬해서 반환하는 함수
# 병합 : 정렬된 작은 두 배열을 합치는 과정 [1,4,6], [2,3,5]
#           >>>>>[1,2,3,4,5,6]
def merge_sort(arr):
    m = len(arr)//2 # 중간 인덱스
    left = arr[:m]
    right = arr[m:]
    # left, right 가 정렬된 상태가 아니니까 정렬



    sorted_arr = []
    return sorted_arr

print(merge_sort(arr))