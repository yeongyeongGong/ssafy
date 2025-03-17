N,M = map(int, input().split()) # N: 기차의 수 M: 명령의 수
train = [[0]*20 for _ in range(N)]
cnt = 0
for i in range(M):
    command = [None] * 3
    command = map(int, input().split())
    print(command)