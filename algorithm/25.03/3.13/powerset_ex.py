# 모든 부분집합의 집합 : power set(멱집합)
# 각 요소에 대해서 부분집합에 포함시키는 경우와 포함시키지 않는 경우 모두 고려
# idx번 요소를 부분 집합에 포함시키는 경우와 포함시키지 않는 경우 모두 수행
def power_set(idx):
    if idx == N:    # 결정할 수 있는 인덱스를 벗어남
        print(subset)
        return

    # idx번 요소를 부분집합에 포함한 경우
    subset.append(arr[idx])
    power_set(idx + 1)
    # idx번  요소를 부분집합에 포함하지 않는 경우
    subset.pop()
    power_set(idx + 1)

arr = ['A','B','C']
N = len(arr)
subset = []
power_set(0)
