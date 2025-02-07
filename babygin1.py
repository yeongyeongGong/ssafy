# num = 456789
num = int(input())
c = [0] * 12  # c[10], c[11]은 항상 0, run 확인을 위한 여분
for _ in range(6):  # 단순 반복 6회(변수 필요 x)
    num % 10  # num%10 -> 1의 자리 알아내기
    num //= 10  # num의 1의 자리 제거

print(c)
