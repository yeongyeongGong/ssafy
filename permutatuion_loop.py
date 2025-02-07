# 순열(Permutation)
# 완전탐색
# 모든 경우의 수를 탐색하기

arr = [1,2,3]
N = len(arr)
perm = [0] * N

# perm 의 0번 칸에 넣을 수 있는거 다 넣어보기
for i in range(N):
    perm[0] = arr[i]
    print(perm)
print('----------------')
# N 개중에 R개 뽑는것 -> 부분집합

check = [0] * N
for i in range(2):
    check[0] = i
    for j in range(2):
        check[1] = j
        for k in range(2):
            check[2] = k
            print(check)
print('----------------')
# greedy(탐욕)
# 완전탐색의 단점은 시간이 오래걸림
# 장점은 모든 경우의 수를 다해보기때문에 정답을 찾기가 쉬움
# 탐욕알고리즘 같은 경우에는 모든 경우를 다 탐색하는 것이 아님
#