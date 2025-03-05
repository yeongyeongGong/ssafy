
# 이진트리에 포화이진트리에
# 번호를 매기는 방식으로 적용
# 루트 노드 : 1
# 왼쪽 자식 : 부모번호 *2
# 오른쪽 자식은 : 부모번호 *2 + 1
H = 2
V = 2 ** (H+1)
tree = [None] * V
tree[1] = 'S'
tree[2] = 'S'
tree[3] = 'A'
tree[4] = 'F'
tree[5] = 'Y'
tree[6] = '!'
tree[7] = '!'
print(tree)
tree_value = [None] *  V
tree_value[5] = 'S'
tree_value[1] = 'S'
tree_value[2] = 'A'
tree_value[3] = 'F'
tree_value[7] = 'Y'
tree_value[6] = '!'
tree_value[4] = '!'
# 인접 리스트 형태로 저장 가능
tree = [[] for _ in range(V)]
tree[1] = [3,7]
tree[2] = [6,4]
tree[5] = [1,2]
# 부모번호를 인덱스로
# 왼쪽자식과 오른쪽 자식을 저장
left = [None] * V
right = [None] * V
left[5] = 1
right[5] = 2
left[1] = 3
left[2] = 6
right[2] = 4
print(left)
print(right)
# 자식 번호를 인덱스로 부모번호를 저장
parent = [None] * V
parent[1] = 5
parent[2] = 5
parent[3] = 1
parent[4] = 2
parent[6] = 2
print(parent)
