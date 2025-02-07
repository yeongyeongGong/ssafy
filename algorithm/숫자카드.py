# 0 ~ 9 까지 적힌 N장의 카드
# N 장의 카드 중에 카드 장수가 제일 많은 숫자와 그 숫자의 카드 수를 출력
# 카드 장수가 동일할 경우 숫자가 큰쪽을 출력

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    card_list = list(map(int, input()))
    count_lst = [0] * 10  # 숫자 a의 범위는 0 <= a <= 10 이므로

    for a in card_list:  # 원본 배열을 순회하면서, a와 같은 인덱스에 1씩 카운트
        count_lst[a] += 1

    max_v = 0               # 최다 숫자카드 숫자 변수
    max_cnt = count_lst[0]  # 최다 숫자카드 갯수 변수

    for i in range(10): # i를 a범위만큼 돌면서 최댓값 찾는 과정처럼 숫자와 갯수 찾기
        if count_lst[i] >= max_cnt:
            max_cnt = count_lst[i]
            max_v = i

        if count_lst[i] == max_cnt:     # 동일한 갯수의 카드가 있다면 그 중에서 가장 큰숫자를 변수에 저장
            if max_v <= i:
                max_v = i

    print(f'#{tc} {max_v} {max_cnt}')
