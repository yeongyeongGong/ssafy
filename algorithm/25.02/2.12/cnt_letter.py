T = int(input())

for tc in range(1, T + 1):
    str1 = list(input())
    str2 = list(input())
    max_values = 0
    str_dict = dict.fromkeys(str1, 0)  # str1의 문자들을 key값으로 변경

    for i in str2:
        if i in str_dict:  # str1에 있는 문자라면 개수 증가
            str_dict[i] += 1
    # value값만 추출해서 그중에 최댓값 구하기
    for value in str_dict.values():
        if value > max_values:
            max_values = value

    print(f'#{tc} {max_values}')
