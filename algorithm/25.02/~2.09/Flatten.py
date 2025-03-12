# 10개의 테스트 케이스
for tc in range(10):
    dump_limit = int(input())  # 덤프 가능 횟수
    box_lines = list(map(int, input().split()))  # 상자 높이 리스트

    # 덤프 한계까지 반복 실행
    for _ in range(dump_limit):
        # 최고점과 최저점 찾기
        highest_idx = 0
        lowest_idx = 0

        for i in range(1, 100):  # 리스트 크기가 100개로 고정
            if box_lines[i] > box_lines[highest_idx]:
                highest_idx = i
            elif box_lines[i] < box_lines[lowest_idx]:
                lowest_idx = i

        # 최고점과 최저점의 차이가 1 이하라면 평탄화 완료 → 중단
        if box_lines[highest_idx] - box_lines[lowest_idx] <= 1:
            break

        # 덤프 수행
        box_lines[highest_idx] -= 1
        box_lines[lowest_idx] += 1

    # 덤프 종료 후 최종 최고점과 최저점 찾기
    highest = max(box_lines)
    lowest = min(box_lines)
    result = highest - lowest

    print(f"#{tc + 1} {result}")
