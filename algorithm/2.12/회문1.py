def count_palindromes(arr, n, m):
    cnt = 0  # 회문 개수

    # 가로 방향 검사
    for i in range(n):  
        for j in range(n - m + 1):  
            for k in range(m // 2):  
                if arr[i][j + k] != arr[i][j + m - 1 - k]:  
                    break
            else:  
                cnt += 1  

    return cnt


T = 10
for tc in range(1, T + 1):
    N = 8  # 8x8 크기의 배열
    M = int(input())  # 찾을 회문의 길이
    word_arr = [input() for _ in range(N)]  # 8줄 입력 받기

    # 가로 방향 검사 + 세로 방향 검사를 zip을 이용해 한 번 더 실행
    result = count_palindromes(word_arr, N, M) + count_palindromes(list(zip(*word_arr)), N, M)

    print(f'#{tc} {result}')
