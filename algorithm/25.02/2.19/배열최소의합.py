# row 행에서 숫자 하나 고르기
def solve(row, tmp_sum):
    global min_v
    # 기존에 알고있던 결과보다 중간결과가 값이 더 크면
    if tmp_sum >= min_v:    # 더 이상의 연산이 의미가 없음(최소값을 구하고 있기 때문)
        # 근데 음수가있으면 완탐해야함, 백트레킹하면 안됨
        return
    if row == N:  # 모든행에서 숫자하나씩 선택완료
        # 행이 없으니 종료
        if tmp_sum < min_v:
            min_v = tmp_sum
        return
    for i in range(N):
        if not used[i]:  # 이전 행에서 사용한 열은 사용하지마
            # arr[row][i] # row 행의 원소 하나
            used[i] = 1  # 사용했으니 사용표시
            solve(row + 1, tmp_sum + arr[row][i])
            used[i] = 0  # 사용 다 했으니 사용표시 지우기


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 각 행마다 모든 열을 선택해보기
    # 그중에서 제일 작은거 고르기...
    min_v = 0xfffffff
    # 같은 열의 값을 선택하지 못하도록 사용표시하는 배열
    used = [0] * N  # 0이면 사용안함, 1이면 사용
    solve(0, 0)
    print(f'#{tc} {min_v}')
