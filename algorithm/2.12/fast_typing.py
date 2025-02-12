def cnt_letter(A, B):
    # B로 A를 돌면서 글자수를 세고
    # B가 있으면 i를 len(B)만큼 증가시키기
    typing_cnt = 0
    longA = len(A)
    longB = len(B)

    for i in range(longA - longB + 1):
        if A[i] != B[0]:
            typing_cnt += 1
        else:  # A[i]와 B의 첫번재 글자가 같다면
            for j in range(longB):
                if B[j] != A[i + j]:
                    break
            else:
                print(i)
                typing_cnt += 1
                i += longB
            print(typing_cnt)
    # return typing_cnt


T = int(input())

for tc in range(1, T + 1):
    A, B = input().split()
    result = cnt_letter(A, B)
    print(f'#{tc} {result}')
