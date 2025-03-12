def numbers(string_arr):
    # 숫자 변환 (인덱스를 사용하여 변경)
    for idx in range(len(string_arr)):
        if string_arr[idx] == 'ZRO':
            string_arr[idx] = 0
        elif string_arr[idx] == 'ONE':
            string_arr[idx] = 1
        elif string_arr[idx] == 'TWO':
            string_arr[idx] = 2
        elif string_arr[idx] == 'THR':
            string_arr[idx] = 3
        elif string_arr[idx] == 'FOR':
            string_arr[idx] = 4
        elif string_arr[idx] == 'FIV':
            string_arr[idx] = 5
        elif string_arr[idx] == 'SIX':
            string_arr[idx] = 6
        elif string_arr[idx] == 'SVN':
            string_arr[idx] = 7
        elif string_arr[idx] == 'EGT':
            string_arr[idx] = 8
        elif string_arr[idx] == 'NIN':
            string_arr[idx] = 9

    # 버블 정렬 (오름차순 수정)
    for i in range(len(string_arr) - 1):
        for j in range(len(string_arr) - 1 - i):
            if string_arr[j] > string_arr[j + 1]:  # 오름차순 정렬
                string_arr[j], string_arr[j + 1] = string_arr[j + 1], string_arr[j]

    # 문자로 다시 변환 (인덱스를 사용하여 변경)
    for idx in range(len(string_arr)):
        if string_arr[idx] == 0:
            string_arr[idx] = 'ZRO'
        elif string_arr[idx] == 1:
            string_arr[idx] = 'ONE'
        elif string_arr[idx] == 2:
            string_arr[idx] = 'TWO'
        elif string_arr[idx] == 3:
            string_arr[idx] = 'THR'
        elif string_arr[idx] == 4:
            string_arr[idx] = 'FOR'
        elif string_arr[idx] == 5:
            string_arr[idx] = 'FIV'
        elif string_arr[idx] == 6:
            string_arr[idx] = 'SIX'
        elif string_arr[idx] == 7:
            string_arr[idx] = 'SVN'
        elif string_arr[idx] == 8:
            string_arr[idx] = 'EGT'
        elif string_arr[idx] == 9:
            string_arr[idx] = 'NIN'

    return string_arr

# 입력 처리
T = int(input())

for tc in range(1, T + 1):
    tc_num, arr_len = input().split()
    string_arr = list(input().split())

    print(tc_num)  # 테스트 케이스 번호 출력
    print(*numbers(string_arr))  # 정렬된 리스트 출력
