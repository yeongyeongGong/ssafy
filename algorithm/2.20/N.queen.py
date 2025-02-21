N = 4
check = [0] * N  # 퀸이 어느 열에 놓여졌는지 표시하는 배열
arr = [['0'] * N for _ in range(N)]
dia1 = [0]*(2*N-1)
dia2 = [0]*(2*N-1)

# row 행에 퀸을 하나 놓아보기

def nqueen(row):
    # row행에서 할 수 있는 경우의 수

    if row == N: #row가 N이 된거는...N-1행 까지 퀸을 놓고
        # N개의 퀸을 놓았다
        for row in arr:
            print(row)
        print('-----------------')
        return  # 퀸 놓 을 필요없음, 행이 끝났음

    # 모든 열에 퀸 놓아보기
    for i in range(N):
        if not check[i] and not dia1[row+i] and not dia2[row - i + N - 1]:
            arr[row][i] = 'q'
            check[i] = 1
            dia1[row+i] = 1
            dia2[row - i + N - 1] = 1
            nqueen(row + 1)  # 다음행에 퀸 놓으러 가기
            # 다음 열에 퀸 놓을거니까... 이번 열에 퀸놓았던거 빼주기
            arr[row][i] = '0'
            check[i] = 0
            dia1[row + i] = 0
            dia2[row - i + N - 1] = 0


nqueen(0)
