def cart(x, y, total_battery):
    global min_battery
    if x >= N or y >= N:    # 경로를 벗어난 경우 return
        return
    if x == y == N-1: # 모든구역을 다 도달한 경우 return
        if total_battery + arr[x][y] < min_battery: # 최소합인지 확인
            min_battery = total_battery + arr[x][y]
            return
    if visited == 0:
        pass




T = int(input())
for tc in range(1, T + 1):
    N = int(input())    # 관리 구역 크기
    arr = [list(map(int, input().split())) for _ in range(N)]   # 관리구역 배열
    min_battery  = 0xffffffff # 최소 배터리 사용량
    visited = [0] * N
    cart(0,0,0)
