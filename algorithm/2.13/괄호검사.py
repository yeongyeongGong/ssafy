# 괄호 지우는 함수
def delete_parentheses(arr):
    stack = []
    for i in arr:
        # i가 종류 상관없이 여는괄호면 stack에 append
        if i == '{' or i == '(':
            stack.append(i)
        # stack이 비어있지 않고, top이 { 일때
        if stack and stack[-1] == '{':
            if i == '}':  # i가 }면 pop으로 제거
                stack.pop()
            else:  # 짝이 맞지않으면 0을 반환
                return 0
        # stack이 비어있지 않고, top이 ( 일때
        if stack and stack[-1] == '(':
            if i == ')':  # i가 )면 pop으로 제거
                stack.pop()
            else:  # 짝이 맞지 않으면 0을 반환
                return 0
            # 닫는괄호로 시작할때
        if (stack and stack[-1] == ')') and (stack and stack[-1] == '}'):
            return 0

    print(stack)
    if stack:
        return 0
    else:
        return 1


T = int(input())
for tc in range(1, T + 1):
    arr = list(input().strip())
    result = delete_parentheses(arr)
    print(f'#{tc} {result}')
