# 문자열 뒤집기
target = 'hello'
N = len(target)
# 앞 뒤 쌍의 자리를 바꿔주기
# 문자열 immutable(변경불가능), 리스트로 만들어주기
target = list(target)
# 중간 전까지만 반복하면서 뒤 요소랑 자리 바꿔주기
mid = N//2
for i in range(mid):
    target[i], target[N-1-i] = target[N-1-i], target[i]

print(target)
# ''.join(target) : target안의 문자열 요소들을 연결
result = '/'.join(target)
print(result) # o/l/l/e/h

# 응용
a = 12345
a = str(a)
a = reversed(a)
print(list(a))
a = ''.join(a)
print(a)
