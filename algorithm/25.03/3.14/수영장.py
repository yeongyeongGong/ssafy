# 가장 적은 비용으로 수영장을 1년간 이용할 수 있는 방법을 찾기
# 가장 적게 지출하는 비용 출력


T = int(input())
for tc in range(1, T + 1):
    cost = list(map(int, input().split()))  # 이용권 금액
    day_plan = list(map(int, input().split()))  # 수영장 계획

