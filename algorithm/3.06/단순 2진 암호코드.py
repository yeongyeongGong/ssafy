codes = ['0001101', '0011001', '0010011', '0111101', '0100011',
         '0110001', '0101111', '0111011', '0110111', '0001011']

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N = 세로, M = 가로
    code_arr = [list(map(int, input().strip())) for _ in range(N)]
    x, y = 0, 0
    found1 = False
    for i in range(N):                  # 모든 코드의 뒷자리는 1으로 끝나기때문에
        for j in range(M - 1, -1, -1):  # 미로의 시작위치를 찾듯 1으로 끝나는 가장 첫번째 좌표를 찾음
            if code_arr[i][j]:
                x, y = i, j
                found1 = True
                break
        if found1:
            break

    find_code = [''] * 8
    print(x,y)
    for k in range(8):
        for l in range(7):
            find_code[k] += str(code_arr[x + k][y - 55 + l])
            # 줄이 안바뀌고 있는것같음,,,,
    print(find_code)

    for i in range(8):
        for j in range(8):
            if find_code[i] == codes[j]:
                find_code[i] = j

    print(find_code)

