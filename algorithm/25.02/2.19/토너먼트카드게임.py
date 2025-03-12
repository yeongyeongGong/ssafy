# 1 ~ N번의 학생 중에 승자 찾기
# start번 부터 end번까지 학생중에 승자를 반환하는 함수
def solve(start, end):
    if start == end:  # 나 밖에 없음
        return start

    mid = (start + end) // 2
    # start 부터 mid까지  학생 중 승자 찾기
    winner1 = solve(start, mid)
    # mid + 1 부터 end 까지 학생중 승자 찾기
    winner2 = solve(mid + 1, end)
    # 둘 중에 누가 이겼는지 반환하기
    result = winner1
    if cards[winner1] == 1 and cards[winner2] == 2:  # 가위
        result = winner2
    elif cards[winner1] == 2 and cards[winner2] == 3:
        result = winner2
    elif cards[winner1] == 3 and cards[winner2] == 1:
        result = winner2
    return result


T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 학생수
    cards = list(map(int, input().split()))
    winner = solve(0, N - 1)
    print(f'#{tc} {winner + 1}')

