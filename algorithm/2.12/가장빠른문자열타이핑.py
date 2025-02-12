def cnt_letter(A, B):
    # B로 A를 돌면서 글자수를 세고
    # B가 있으면 i를 len(B)만큼 증가시키기
    typing_cnt = 0
    longA = len(A)
    longB = len(B)

    i = 0
    while i > longA - longB + 1:
        if A[i] != B[0]:
            pass







T = int(input())

for tc in range(1, T + 1):
    A, B = map(int, input().split())

    result = cnt_letter(A, B)


    print(f'#{tc} {result}')