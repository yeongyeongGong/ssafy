# 특별한 정렬
# 가장 큰 수 , 가장 작은수, 2번째 큰수, 2번째 작은수....
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    lst_a = list(map(int, input().split()))
    sort_lst = []
    for num in range(5):  # 10개 출력하라했고, 한번에 최소,최대 동시에 출력됨으로 5번 반복
        max_num = 1  # 배치 되지 않은 숫자중에 최댓값
        min_num = 100  # 배치 되지 않은 숫자중에 최솟값

        # 최대값 최소값을 찾기
        for i in lst_a:
            if i > max_num:
                max_num = i
            if i < min_num:
                min_num = i

        # 찾은 최대값, 최소값을 새로운 배열에 순서대로 넣기
        sort_lst.append(max_num)
        sort_lst.append(min_num)
        # 배열에 넣은 최대값, 최소값은 remove로 제거
        lst_a.remove(max_num)
        lst_a.remove(min_num)

    print(f'#{tc} {" ".join(map(str, sort_lst))}')
