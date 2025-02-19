# 연결 큐 : 노드끼리 연결된 형태의 큐
# front만 저장하고 있으면
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.front = None

    def enqueue(self, data):
        # 맨 마지막 요소 찾아서 거기에 새로운 노드 달아주기
        new_node = Node(data)
        if self.front is None:
            self.front = Node(data)
        else:
            last = self.front
            next = last.next
            while next is not None:
                last = next
                next = last.next
            last.next = new_node

    def dequeue(self):
        # front 삭제
        return_value = self.front.data
        self.front = self.front.next
        return return_value

queue = LinkedQueue()
queue.enqueue('A')
queue.enqueue('B')
queue.enqueue('C')
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())