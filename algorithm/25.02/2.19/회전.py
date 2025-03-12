T = int(input())  # 테스트 케이스 개수 입력

for t in range(1, T + 1):
    N, M = map(int, input().split())  # N: 숫자 개수, M: 이동 횟수
    numbers = list(map(int, input().split()))  # 리스트로 입력받기

    # M번 회전 (맨 앞 요소를 맨 뒤로 보냄)
    for _ in range(M):
        first = numbers[0]  # 맨 앞 원소 저장
        numbers = numbers[1:] + [first]  # 슬라이싱을 이용한 회전

    print(f"#{t} {numbers[0]}")  # 맨 앞 숫자 출력
