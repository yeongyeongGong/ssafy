def find_page(end_page, a_page, b_page):
    end_page = end_page
    start = 1
    find_mid = (end_page + start) / 2
    cnt_a = 0  # a가 탐색한 횟수
    cnt_b = 0  # b가 탐색한 횟수

    # a의 페이지 탐색
    # find_mid와 동일해질때까지 반복
    while find_mid == a_page:
        if a_page > find_mid:
            cnt_a += 1
            start = find_mid
        elif a_page < find_mid:
            cnt_a += 1
            end_page = find_mid
    # b의 페이지 탐색
    # find_mid와 동일해질때까지 반복
    while find_mid == b_page:
        if b_page > find_mid:
            cnt_b += 1
            start = find_mid
        elif b_page < find_mid:
            cnt_b += 1
            end_page = find_mid
    return cnt_a


T = int(input())

for tc in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())
    print(find_page(P, Pa, Pb))
