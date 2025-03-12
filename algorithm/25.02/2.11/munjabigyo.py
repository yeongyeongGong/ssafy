T = int(input())

for tc in range(1, T + 1):
    str1 = list(map(str, input()))
    str2 = list(map(str, input()))
    n, m = len(str1), len(str2)

    for i in range(m - n + 1):  # str2에서 str1의 길이를 뺀만큼 반복
        instr2 = 0
        for j in range(n):
            if str1[j] == str2[i + j]:  # str[j]가 str2안에 있는지 확인
                break  # 없으면 break
        instr2 = 1  #

    print(f'#{tc} {instr2}')
# --------------------위에는 내가 한거 작동안됨;;;;

def solve(str1, str2):
    for i in range(N - M + 1):  # i: 비교하려는 시작 인덱스
        is_find = True
        for j in range(M):  # 검사 인덱스
            # str1[j]과 str2[i + j]를 비교
            if str1[j] != str2[i + j]:  # 다르면 검사 종료
                is_find = False
                break
        # else: # break 문이 안걸렸을 때 실행하는 문장 : 아래와 동일하지만 또다른 표현식
        #     return 1
        if is_find:  # True 값을 유지하고 있으면 str2에 str1이 포함
            return 1
    # 반복문 다 도는 동안 매칭되는게 없었으면 0 반환
    return 0


T = int(input())
for tc in range(1, T + 1):
    str1 = input()
    str2 = input()
    N = len(str2)  # 긴 문자열의 길이
    M = len(str1)  # 짧은 문자열의 길이


    result = solve(str1, str2)
    print(f'#{tc} {result}')
