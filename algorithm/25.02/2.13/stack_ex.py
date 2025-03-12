# stack을 만들기 위해서 필요한 거
# 1. 리스트 : 데이터를 저장하는 목적
# 2. top 변수 : stack의 마지막 요소를 가리키는 변수
# 3. push, pop
class MyStack:
    #상태값 : 리스트, top
    def __init__(self,length):
        self.max_size = length
        self.s = [None] * length
        self.top = -1

    def is_empty(self):
        if self.top == -1:
            return True
        return False
    def is_full(self):
        if self.top + 1 == self.max_size:
            return True
        return False

    def push(self,data):
        if not self.is_full():
            self.top += 1
            self.s[self.top] = data
        else:
            print('가득 찼는데요?')

    def pop(self):
        if not self.is_empty():
            value = self.s[self.top]
            self.top -= 1
            return  value
        return None

# stack = MyStack(5)
# stack.push('A')
# stack.push('B')
# stack.push('C')
# stack.push('D')
# stack.push('E')
# # stack.push('F')
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# # print(stack.pop())
stack = []
stack.append('A')
stack.append('B')
stack.append('C')
stack.append('D')
stack.append('E')
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())

stack = [None] * 10000
top = -1
top += 1
stack[top] = 'A'
top += 1
stack[top] = 'B'
top += 1
stack[top] = 'C'
top += 1
stack[top] = 'D'
top += 1
stack[top] = 'E'

print(stack[top])
top -= 1
print(stack[top])
top -= 1
print(stack[top])
top -= 1
print(stack[top])
top -= 1
print(stack[top])
top -= 1



