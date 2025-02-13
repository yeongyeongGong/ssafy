# 문자 지우는 함수
def delete_letter(arr):
    n = len(arr)

    if n == 0:
        return 0  # 남은 문자열이 없으면 0을 출력

    lst = []
    for i in arr:
        # lst 비어있지 않고, lst 마지막인덱스가
        # i와 똑같은 문자이면 lst[-1]요소 제거
        if lst and lst[-1] == i:
            lst.pop()
        else: # lst 비어있거나, 마지막인덱스가 i와 같지않으면
            lst.append(i) # lst i 추가

    return len(lst)


T = int(input())

for tc in range(1, T + 1):
    arr = list(input())

    result = delete_letter(arr)

    print(f'#{tc} {result}')
