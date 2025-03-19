# idx 번째 직원이 모든 업무에 대해서 할당 받는 경우의 수 고려
# tmp_rate : 여태까지 누적 성공확률
def solve(idx, tmp_rate):

    global max_rate
    if tmp_rate < max_rate: # 중간 계산결과가 이미 더 낮으므로, 계산필요 x
        return
    if idx == N:    # 모든 직원에 대해서 업무 배당 완료
        # 계산한 누적 성공확률이 최대성공확률보다 크면
        # 최대 성공확률 바꿔주기
        if max_rate < tmp_rate:
            max_rate = tmp_rate

        for i in range(N):
            # data[idx][i] :  idx 번째 직원이 i번 업무를 했을 때 성공할 확률
            if check[i] == 0:   # i 번 직원이 아직 업무할당이 안됭었으면
                check[i] = 1
                solve(idx+1, tmp_rate* data[idx][i])
                check[i] = 0




T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data =  [list(map(int, input().split())) for _  in range(N)]
    check = [0] * N # 동일 업무 할당을 방지하기 위한 체크 배열
    for i in range(N):
        data[i][j] = data[i][j]/100

    max_rate = 0
    solve(0,1)
    print(f'#{tc} {max_rate * 100:.6f}')