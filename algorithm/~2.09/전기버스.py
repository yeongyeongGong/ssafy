# 노선 수
T = int(input())
for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    charge_place = list(map(int, input().split()))
    charge_cnt = 0  # 충전 횟수
    charger_index = 0  # 지나친 충전 정류장 갯수

    # 현재위치에서 종점까지 이동
    for now_locate in range(N + 1):
        for charger in charge_place:  # 충전소 위치 리스트를 개별요소로 빼기
            if now_locate <= charger <= now_locate + K:  # 정류소 위치가 현재 위치랑, 현재위치 + 이동가능한 수 사이에 존재하면
                # 만약에 범위안에 존재하는 정류장이 2개이상이면 더 큰 인덱스에 위치한 정류소로 이동
                # 이 경우 charger_index 를 += 1만 하면안됨
                # 지나친 모든 경우의 정류장 갯수를 더해줘야함

                # if :
                    now_locate = charger  # 현재 위치를 해당 정류소 위치로 변경
                    charge_cnt += 1
                    pass