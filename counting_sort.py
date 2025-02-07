'''
0<=DATA[i]<=4 조건
'''

DATA = [0,4,1,3,1,2,4,1]
N = len(DATA)
COUNTS = [0] * 5 # max(DATA) + 1, 크기에 주의!!

for i in range(N):  # 각 숫자의 개수
    COUNTS[DATA[i]] += 1

print(COUNTS)
