# 100 * 100 배열 생성 후
# 색종이가 있는곳은 값을 1로 변경
# 1으로 변경된 칸 갯수 -> 색종이 너비

T = int(input())
paper = [[0] * 100 for _ in range(100)]
cnt = 0
for _ in range(T):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = 1

for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            cnt += 1

print(cnt)