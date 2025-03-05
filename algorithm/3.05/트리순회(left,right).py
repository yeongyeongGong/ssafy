# 트리 저장은 배열에 할 거에요
left = [None] * 16
right = [None] * 16
left[1] = 2
right[1] = 3
left[2] = 4
left[3] = 6
right[3] = 7
left[6] = 12
right[6] = 13


# 트리의 모든 노드를 순회
# 전위순회 : 루트노드에서 작업처리(방문)하고, 왼쪽 서브트리, 오른쪽 서브트리 순서로 방문
# v번 노드에서 작업처리하기
def preorder(v):
    if v is None:
        return
    print(v, end='  ')
    preorder(left[v])
    preorder(right[v])


preorder(1)
print()
# 중위순회 :
# v번에서 작업처리
def inorder(v):
    if v is None:
        return
    inorder(left[v])
    print(v, end='  ')
    inorder(right[v])


inorder(1)
print()
# 후위순회 :
# v번에서 작업처리
def postorder(v):
    if v is None:
        return
    postorder(left[v])
    postorder(right[v])
    print(v, end='  ')


postorder(1)
print()