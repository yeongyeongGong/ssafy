# 순열
arr = ['a', 'b', 'c']
N = len(arr)
perm = [None] * N

used = [0] * N  # 0은 사용 안한거 1은 사용한거


# idx 번째에 모든 요소 넣어보기
def permutation(idx):
    if idx == N:
        print(perm)
        return
    for i in range(N):
        if not used[i]:
            perm[idx] = arr[i]
            used[i] = 1
            permutation(idx + 1)
            used[i] = 0


permutation(0)
