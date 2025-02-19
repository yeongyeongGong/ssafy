arr = [1, 2, 3, 4, 5]
N = len(arr)
M = 3
# 각 요소가 조합에 포함되는지 아닌지 표시하는 배열
check = [0] * N

#외워,,,,,,,,,,,,,,, combination, powerset, permutation 외,,,,,,,워,,,,^^
#DFS, BFS, 조합, 집합, 순열 + 반복문 공부해라공부해~~!!!!!!
# check의 각 idx에 0 또는 1을 넣을건데 ... 몇 개가 포함되는지 알아야한다.
def combination(idx, cnt):
    if cnt == M:
        print(check)
        return
    if idx == N:    # 정답을 찾지 못한 상태, 마지막 인덱스까지 M개의 요소를 선택하지 못함
        # print(check)
        # cnt = 0
        # for i in range(N):  # 요소가 몇개 포함되었는지 확인
        #     if check[i]:
        #         cnt += 1
        # if cnt == M:
        #     print(check)
        return
    check[idx] = 0
    combination(idx + 1, cnt)  # 하나의 상태를 확정하면 다음 인덱스 결정하러 ㄱㄱㄱ
    check[idx] = 1
    combination(idx + 1, cnt + 1)
    check[idx] = 0


combination(0,0)
