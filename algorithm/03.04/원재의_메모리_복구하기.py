T = int(input())

for tc in range(1, T + 1):
    memory = list(map(int, input()))
    init_memory = [0] * len(memory)
    cnt = 0
    for i in range(len(memory)):
        if memory[i] != init_memory[i]:
            for j in range(i,len(memory)):
                init_memory[j] = 1-init_memory[j]
            cnt += 1
        else:
            continue

    print(f'#{tc} {cnt}')