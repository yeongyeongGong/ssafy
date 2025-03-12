# 후위 표기법
# 우선순위가 높은 연산자가 먼저 나오는 방법
# 2 + 4 * 3     ->     243*+
# (괄호를 읽을 때는 우선순위가 높은데)
# 괄호 안의 연산자는 괄호가 처리되기 전에 먼저 연산되어야 함
# (이미 읽혀진 괄호는 처리가 늦게 되어야 한다(우선순위가 낮아야한다.))
# incoming priority
icp = {
    '*': 2, '/': 2, '+': 1, '-': 1, '(': 3
}
# in stack priority
isp = {
    '*': 2, '/': 2, '+': 1, '-': 1, '(': 0
}
exp = '(6+5*(2-8)/2)'
stack = []
for ch in exp:  # 토큰 하나씩 읽어오기
    # 연산자의 우선순위가 높은게 먼저 나와야 한다!
    if ch in '013456789':  # 읽은게 숫자다 >> 출력
        print(ch, end='')
    elif ch == ')': # 닫히는 괄호라면 여는 괄호가 나올 때까지 pop하면서 연산자 출력
        while stack[-1] != '(':
            print(stack.pop(), end='')
        # 여는 괄호는 버리기
        stack.pop()
    else:  # 연산자라면 스택에 넣아야 한다.
        # 근데 ... 우선순위가 높은애는 빼고 넣어야 한다.
        if not stack:  # 스택이 비었으면 그냥 넣으면 된다.
            stack.append(ch)
        else:  # 스택이 비어있지 않다면
            # ch보다 우선순위가 높거나 같은 연산자는 출력하고 스택에 ch를 push
            while stack and isp[stack[-1]] >= icp[ch]:
                print(stack.pop(), end='')
            stack.append(ch)

while stack:    # 남아있는 연산자 모두 출력
    print(stack.pop(), end='')