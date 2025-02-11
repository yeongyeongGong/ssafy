def number(string_arr):
    # 문자에 각각 0~9까지 숫자 배정
    for i in string_arr:
        if i == 'ZRO':
            i = 0
        elif i == 'ONE':
            i = 1
        elif i == 'TWO':
            i = 2
        elif i == 'THR':
            i = 3
        elif i == 'FOR':
            i = 4
        elif i == 'FIV':
            i = 5
        elif i == 'SIX':
            i = 6
        elif i == 'SVN':
            i = 7
        elif i == 'EGT':
            i = 8
        elif i == 'NIN':
            i = 9

