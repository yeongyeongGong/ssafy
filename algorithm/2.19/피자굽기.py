T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    input_lst = list(map(int, input().split()))
    pizza_list = [el for el in enumerate(input_lst, start=1)]
    print(pizza_list)
    queue = []  # 화덕
    # pizza_lst = []
    # for i in range(M):
    #     input_lst[i] # input_lst[i] >> 치즈양, i+1: 피자 번호
    #     pizza_lst.append((i+1, input_lst[i]))
    for i in range(N):  # 화덕의 크기 만큼 피자 넣기
        queue.append(pizza_list[i])

    next = N  # 문제 조건에 따라서 N개의 피자가 화덕에 들어감
    # 다음에 들어갈 피자는 N번 피자
    while len(queue) > 1:  # 피자가 하나 남을 때 까지 화덕 가동
        num, cheese = queue.pop(0)
        cheese = cheese // 2
        if cheese == 0:  # 치즈가 다녹음 : 얘는 빼고 새로운 피자 넣기
            # if 남아있는 피자가 있으면 넣기
            if next < M:
                queue.append(pizza_list[next])
                next += 1
        else:  # 치즈가 덜 녹음
            queue.append((num, cheese))

    last_pizza = queue.pop(0)
    print(f'#{tc} {last_pizza[0]}')
