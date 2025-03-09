arr = [list(map(int, input().split())) for _ in range(9)]
max_val = arr[0][0]
x,y = 0,0
for i in range(9):
    for j in range(9):
        if arr[i][j] > max_val:
            max_val = arr[i][j]
            x,y = i+1, j+1

print(max_val)
print(x, y)