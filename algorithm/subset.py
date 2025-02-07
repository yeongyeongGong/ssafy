# sub_set(부분집합) 구하기
# 모든 부분집합의 집합 >> power_set(멱집합)
arr = ['a', 'b', 'c']
N = len(arr)
check = [0] * N  # 요소가 부분집합에 포함되는지 아닌지를 0 또는 1로 표시하는 배열
# ex) check = [1,0,1] >>> ['a','c']
# 0번 인덱스에 0또는 1 넣기
for i in range(2):  # i : 0 또는 1
    check[0] = i
    for j in range(2):
        check[1] = j
        for k in range(2):
            check[2] = k
            print(check)
            # check의 요소가 1이면 출력, 0이면 출력 x
            for a in range(N):
                if check[a]:
                    print(arr[a], end=',')
            print() # 부분집합 하나 출력 끝났으니 한 줄 내려주기 (줄바꿈)
            #        <- 공집합도 출력됨
            # c,
            # b,
            # b, c,
            # a,
            # a, c,
            # a, b,
            # a, b, c,

# 알고리즘 문제의 기본 >>> 
# 완전탐색 : 배열 순회, 순열, 조합, 집합....