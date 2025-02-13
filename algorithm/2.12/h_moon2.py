# arr에서 가장 긴 길이의 회문을 반환하는 함수
def solve(arr):
    #M의 길이가 고정되어있다고 가정했을 때 코드부터..
    M = 5
    max_length = 1
    for i in range(N):
        is_find = False
        for M in range(N,1,-1): # 회문의 길이를 줄여나가는 반복문

            for j in range(N + M + 1):  #검사 시작점 이동 반복문
                is_pal = True
                for k in range(M//2):
                    if arr[i][j] != arr[i][j+M-1-k]:
                        is_pal = False
                        break
                if is_pal:  #회문인지 확인
                    # 회문이다!!!
                    if max_length < M:
                        max_length = M
                    is_find = True
                    break
            if is_find: # 검사 회문 길이 M을 줄이는 반복문 종료
                break
        ###############열검사###########################
            is_pal = True
            for k in range(M // 2):
                if arr[j][i] != arr[j + M - 1 - k][i]:
                    is_pal = False
                    break
            if is_pal:  # 회문인지 확인
                # 회문이다!!!
                if max_length < M:
                    max_length = M
                is_find = True
                break
        if is_find:  # 검사 회문 길이 M을 줄이는 반복문 종료
            break

    return max_length


T = 10
for _ in range(T):
    tc = input()
    N = 100
    arr = [input() for _ in range(N)]

    result = solve(arr)
    print(f'#{tc} {result}')