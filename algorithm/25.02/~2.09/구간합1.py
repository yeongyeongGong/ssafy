T = int(input())

for tc in T:
    N, M = map(int, input().split())
    V = list(map(int, input().split()))

min_v = sum(V[:M])
max_v = sum(V[:M])
for i in range(N - M + 1):
    # i 번에서 시작하는 길이 M짜리 구간 반복
    sum_v = 0
    for j in range(i, i + M):
        sum_v += V[j]
    if sum_v > max_v:
        max_v = sum_v
    if sum_v < min_v:
        min_v = sum_v

print(f'#{tc} {max_v - min_v}')