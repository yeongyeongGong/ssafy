def bfs():
    front, rear = 1, 1
    queue = [None] * 1000000

    # N을 몇 번 연산해야 M을 만들 수 있냐?
    # queue = [(N, 0)]

    def enqueue(data):
        nonlocal rear, front
        rear = (rear + 1) % 1000000
        queue[rear] = data

    def dequeue():
        nonlocal front, rear
        front = (front + 1) % 1000000
        return queue[front]

    enqueue((N, 0))
    # 한 번 연산 해봤던 숫자들은 연산 다시 안하기.....
    check = [0] * 1000001
    while queue:
        num, cnt = dequeue()
        if num < 0 or num > 1000000 or check[num]:  # 더이상 연산 불필요
            continue
        if num == M:
            return cnt
        check[num] = 1
        # num을 이용해서 할 수 있는 연산 다 넣어보기
        enqueue((num + 1, cnt + 1))
        enqueue((num - 1, cnt + 1))
        enqueue((num * 2, cnt + 1))
        enqueue((num - 10, cnt + 1))
        # queue.append((num + 1, cnt + 1))
        # queue.append((num - 1, cnt + 1))
        # queue.append((num * 2, cnt + 1))
        # queue.append((num - 10, cnt + 1))
    # 실행 가능성 없지만..그냥 넣어주기 이쁘니까
    return -1


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    result = bfs()
    print(f'#{tc} {result}')
