# 가로의 길이가 증가함에 따라 이전 가로의 길이에 새로운 종이 붙여나가기
# 길이가 N인 종이의 경우의 수를 반환하는 함수
# f(N) = f(N-1) + f(N-2)*2
def paper(N):
    if N == 10:
        return 1
    elif N == 20:
        return 3

    return paper(N - 10) + paper(N - 20) * 2


# dp로 푸는함수
def peper2(N):
    N = N // 10
    memo = [0] * 30
    memo[1] = 1
    memo[2] = 3
    for i in range(3, N + 1):
        memo[i] = memo[i - 1] + memo[i - 2] * 2
    return memo[N]

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    result = paper(N)

    print(f'#{tc} {result}')
