# 선형큐
N = 10
queue = [None] * N
# 삽입 위치와 삭제위치가 달라서 변수 2개가 필요
front = rear = -1
# 삽입(enqueue) : rear 를 1 증가시키고 그 위치에 요소 삽입
# 삭제(dequeue): front를 1 증가시키고 그 위치의 요소를 반환
#       (진짜 삭제는 아니고 재사용 못하는 상황)
def enqueue(data):
    # rear 를 1 증가시키고 그 위치에 요소 삽입
    global rear
    if rear == N-1:
        print('큐가 가득 찼어요')
    else:
        rear += 1
        queue[rear] = data

def dequeue():
    global front
    if front == rear:
        print('큐가 비었습니다!')
    else:
        front += 1
        return queue[front]
# 선형 큐
# 큐가 비었는지 어떻게 확인? front와 rear가 같으면 비어있는거
# 큐가 가득찬 경우는 rear가 배열의 마지막 인덱스를 가리키면 가득 찬 상태

enqueue(5)
enqueue(4)
enqueue(3)
enqueue(2)
enqueue(1)
enqueue(5)
enqueue(4)
enqueue(3)
enqueue(2)
enqueue(1)
print(dequeue())
print(dequeue())
print(dequeue())
print(dequeue())
print(dequeue())
print(dequeue())
print(dequeue())
print(dequeue())
print(dequeue())
print(dequeue())
enqueue(1)
print(dequeue())
