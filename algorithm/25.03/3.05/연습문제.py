V = int(input())
tree = [[None,None] for _ in range(V+1)]
edges = list(map(int,input().split()))
for i in range(0,(V-1)*2,2):
    # edges[i] : 부모  edges[i+1] : 자식번호
    # tree의 부모인덱스에 자식 번호가 저장
    if tree[edges[i]][0] is None:
        tree[edges[i]][0] = edges[i+1]
    else:
        tree[edges[i]][1] = edges[i + 1]

def preorder(v):
    if v is None:
        return
    print(f'{v}번 방문!', end=' ')
    preorder(tree[v][0])
    preorder(tree[v][1])

preorder(1)



# 13
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
