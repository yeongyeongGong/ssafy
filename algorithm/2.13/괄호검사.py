def delete_parentheses(arr):
    stack = []
    for i in arr:
        # 여는 괄호는 스택에 추가
        if i == '{' or i == '(':
            stack.append(i)
        # 닫는 괄호를 만나면 스택이 비어있는지 먼저 체크
        elif i == '}':
            if not stack or stack[-1] != '{':  # 스택이 비었거나 짝이 안 맞으면
                return 0
            stack.pop()  # 짝이 맞으면 pop()
        elif i == ')':
            if not stack or stack[-1] != '(':  # 스택이 비었거나 짝이 안 맞으면
                return 0
            stack.pop()  # 짝이 맞으면 pop()

    # 스택이 비어 있으면 짝이 맞음 → 1 반환, 남아 있으면 짝이 안 맞음 → 0 반환
    return 1 if not stack else 0


T = int(input())
for tc in range(1, T + 1):
    arr = list(input().strip())
    result = delete_parentheses(arr)
    print(f'#{tc} {result}')
