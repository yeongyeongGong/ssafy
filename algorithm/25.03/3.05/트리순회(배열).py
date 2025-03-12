# 트리 저장은 배열에 할 거에요
tree = [None] * 16
tree[1] = 'A'
tree[2] = 'B'
tree[3] = 'C'
tree[4] = 'D'
tree[6] = 'E'
tree[7] = 'F'
tree[12] = 'G'
tree[13] = 'H'


# 트리의 모든 노드를 순회
# 전위순회 : 루트노드에서 작업처리(방문)하고, 왼쪽 서브트리, 오른쪽 서브트리 순서로 방문
# v번 노드에서 작업처리하기
def preorder(v):
    if v > 15 or tree[v] is None:   # 해당번호 노드가 없으면...
        return
    # 왼쪽자식 : v(현재노드번호) * 2
    # 오른쪽자식 : v(현재노드번호) * 2 + 1
    print(f'{v}번 : {tree[v]}', end='  ')
    preorder(v * 2) # 왼쪽자식 작업 처리
    preorder(v * 2 + 1) # 오른쪽자식 작업처리

preorder(1)
print()
# 중위순회 :
# v번에서 작업처리
def inorder(v):
    if v > 15 or tree[v] is None:
        return
    inorder(v * 2)
    print(f'{v}번 : {tree[v]}', end='  ')
    inorder(v * 2 + 1)
inorder(1)
print()
# 후위순회 :
# v번에서 작업처리
def postorder(v):
    if v > 15 or tree[v] is None:
        return
    postorder(v * 2)
    postorder(v * 2 + 1)
    print(f'{v}번 : {tree[v]}', end='  ')
postorder(1)
print()