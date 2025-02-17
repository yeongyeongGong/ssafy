# 전등의 갯수
N = int(input())
arr = [0] + list(map(int, input().split()))
# 학생수
M = int(input())
for _ in range(M):
# 성별, 번호
g, num = map(int, input().split())
# g가 1인 경우, num 부터 num의 배수에 해당하는 스위치 상태 바꾸기
# g가 2인 경우,
if g == 1:
    for i in range(num, N, num):
        arr[i] = 1 - arr[i]

if g == 2:
    # 양쪽 대칭이 아니더라도 그 자리는 바뀌니까.. 바꾸고 시작
    arr[num] = 1 - arr[num]
    step = 1
    # 정상 범위 안에 있으면서 대칭인 요소가 같으면 바꿔주기
    while (num - step > 0 and num + step < N) and arr[num - step] == arr[num + step]:
        arr[num - step] = 1 - arr[num - step]
        arr[num + step] = 1 - arr[num + step]
        step += 1  # 바꿨으니까 한 칸 옆으로...

for i in range(1, N + 1):
    print(arr[i], end=' ')
    if i % 20 == 0:
        print()
