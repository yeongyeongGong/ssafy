# heap의 특징 :
# 1. 부모노드가 자식노드보다 항상 크다(혹은 항상 작다)
# 2. 완전이진트리를 유지 1번부터 번호 매길때... 빈번호가 없음
heap = [0] * 10
heapcount = 0  # heap의 마지막 요소를 가리키는 변수


def heappush(data):
    global heapcount
    # 1. 완전 이진트리의 마지막에 요소 추가
    # 2. 부모요소랑 값비교 하면서 자리바꿔주기 * 반복
    #    (루트 또는 부모가 더 클 때 까지)
    heapcount += 1
    heap[heapcount] = data
    current = heapcount
    parent = current // 2
    while True:
        if current == 1 or heap[current] < heap[parent]:
            break
        if heap[current] > heap[parent]:
            heap[current], heap[parent] = heap[parent], heap[current]
        current = parent
        parent = current // 2

# heappop
# 1. 루트 반환 및 삭제
# 2. 마지막 요소를 루트에 올리기
# 3. 자식들 중 큰 값이랑 비교해서 작으면 바꾸기(내가 더 크거나 혹은 내가 단말 노드라면 중지)
def heappop():
    global heapcount
    result = heap[1]    # 기존 루트 저장
    heap[1] = heap[heapcount]   # 마지막 요소 루트에 넣기
    heapcount -= 1
    # heap 모양 만들어주기
    # 자식들 중 큰 거랑 바꾸기...
    current = 1
    child = current * 2
    while True:
        if child > heapcount:  # 자식이 없으면
            break
        if (child + 1) <= heapcount: #오른쪽 자식이 있으면...
            if heap[child+1] > heap[child]: # 오른쪽이 더 크면...
                child += 1  # 오른쪽 자식 위치를 선택
        if heap[child] > heap[current]:
            heap[child], heap[current] = heap[current], heap[child]
        else:
            break
        current = child
        child = current * 2

    return result


heappush(2)
print(heap)
heappush(5)
print(heap)
heappush(7)
print(heap)
heappush(4)
print(heap)
heappush(10)
print(heap)
heappush(11)
print(heap)

print(heappop())
print(heap)
print(heappop())
print(heap)
print(heappop())
print(heap)
print(heappop())
print(heap)
