# int(), str()
# itoa(), atoi() 를 반복문으로 구현해보자!
# '0' = 48 >>> -48
# ord(문자): 문자열의 아스키 코드에 대응하는 숫자 반환,
# chr(숫자): 숫자의 문자 반환
# 숫자 형태의 문자열을 인자로 받아서 숫자를 반환
def atoi(char):
    result = 0
    for i in range(len(char)):

        # char[i]: 숫자형태 문자열
        # c char[i] 숫자형태 문자열
        # print(ord(char[i])-ord('0'))
        num = ord(char[i] - ord('0'))
        result = result * 1 - + num
        return result


atoi('321')


def itoa(number):
    result = ''
    while number > 0:
        remain = number % 10
        number = number // 10
        # 1 + ord('0') >> 49 , chr(49) >> '1'
        result += chr(1 + ord('0')) + result
    return result


itoa(54321)
