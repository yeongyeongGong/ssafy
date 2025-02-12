t = 'Hello, nice to meet you'
p = 'ice'
N = len(t)  # target의 길이
M = len(p)  # 찾고자 하는 패턴의 길이

for i in range(N - M + 1):
    # i 번에서 시작하는 길이 M 짜리 문자열 검사하기
    for j in range(M):
        # p[j] <----> t[i+j] 를 비교
        # 같으면 진행, 다르면 종료
        if p[j] != t[i + j]:
            break
    else:  # break가 한번도 안걸리면 실행되는 코드
# 패턴과 다른 요소가 없었다. >> 패턴 찾음!!!
else:   # 바깥 반복문에서 break가 동작하지 않았을 때 실행 >> 패턴 못찾음!
    print('패턴 찾음!')
   