## 함수,클래스(대문자)
## C, C++ --> 변수이름 규칙의 원본
## 실무 : 변수 이름 규정 --> 여러분이 지정
## 구글링을 통해서 좋은 변수명 규칙 --> 적용

def isQueueFull() :
    global SIZE, queue, front, rear
    if (rear != SIZE-1) :
        return False
    if (rear == SIZE -1) and (front == -1) :
        return True
    else:
        for i in range(front+1, SIZE) :
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
        return False


def enQueue(data):
    global SIZE, queue, front, rear
    if (isQueueFull()) :
        print('큐 꽉!')
        return
    rear += 1
    queue[rear] = data

def isQueueEmpty() :
    global SIZE, queue, front, rear
    if (front == rear) :
        return True
    else:
        return False

def deQueue() :
    global SIZE, queue, front, rear
    if (isQueueEmpty()) :
        print('큐 텅!')
        return None
    front += 1
    data = queue[front]
    queue[front] = None
    return data

def peek() :
    global SIZE, queue, front, rear
    if (isQueueEmpty()) :
        print('큐 텅!')
        return None
    return queue[front+1] # 다음 데이터 파악하기

## 변수
SIZE = int(input('큐 크기를 입력하세요 -->'))
queue = [None for _ in range(SIZE)]
front, rear = -1, -1

## 메인
# queue = [None,None,'문별','휘인',None]
# front = 1
# rear = 3
# print(queue)
# enQueue('선미')
# print(queue)
# enQueue('재남')
# print(queue)
#
# queue = ['화사',None,None,None,None]
# front = -1
# rear = 0
# print(queue)
# retData = deQueue()
# print('추출 -->',retData)
# retData = deQueue()
# print('추출 -->',retData)
# print(queue)

if __name__ == '__main__' :
    select = input('삽입(I)/추출(E)/확인(V)/종료(X) 중 하나 선택 -->')
    while (select != 'X' and select != 'x') :
        if (select == 'I' or select == 'i') :
            data = input('입력할 데이터 -->')
            enQueue(data)
            print('큐 상태 : ',queue)
        elif (select == 'E' or select == 'e') :
            data = deQueue()
            print('추출된 데이터 -->',data)
            print('큐 상태 : ',queue)
        elif (select == 'V' or select == 'v') :
            data = peek()
            print('확인된 데이터 -->', data)
            print('큐 상태 : ', queue)
        else:
            print('입력이 잘못됨!')
        select = input('삽입(I)/추출(E)/확인(V)/종료(X) 중 하나 선택 -->')
    print('프로그램 종료!')