T = int(input())

for tc in range(1, T + 1):
    E, N = map(int, input().split())  # E = 간선 갯수, N = 서브트리의 루트
    node = list(map(int, input().split()))
    left = [0] * (max(node) + 1)
    right = [0] * (max(node) + 1)

    for i in range((len(node) // 2)):
        node_num = node[2 * i]
        if left[node_num] == 0:
            left[node_num] = node[2 * i + 1]
        else:
            right[node_num] = node[2 * i + 1]

    print(left)
    print(right)
