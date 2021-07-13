## 함수
def isStackFull():
    global SIZE, stack, top
    if top >= SIZE -1 :
        return True
    else:
        return False

def isStackEmpty():
    global SIZE, stack, top
    if top <= -1 :
        return True
    else:
        return False

def pop() :
    global SIZE, stack, top
    if (isStackEmpty()) :
        print('스택 텅!')
        return
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

def push(data):
    global SIZE, stack, top
    if (isStackFull()) :
        print('스택 꽉!')
        return
    top += 1
    stack[top] = data

def peek():
    global SIZE, stack, top
    if (isStackEmpty()) :
        print('스택 텅!')
        return None
    return stack[top]

## 전역
SIZE = int(input('스택 크기 입력하세요-->'))
stack = [None for _ in range(SIZE)]
top = -1

## 결과 확인
# stack = ['커피','녹차','꿀물','콜라','환타']
# top = 4
# stack = ['커피','녹차','꿀물','콜라',None]
# top = 3
#
# print(stack)
# push('개토레이')
# print(stack)
# push('파워에이드')
# print(stack)
#
# stack = ['커피',None,None,None,None]
# top = 0
# retData = pop()
# print(retData)
# retData = pop()
# print(retData)

## 메인
if __name__ == '__main__' :
    select = input('삽입(I)/추출(E)/확인(V)/종료(X) 중 하나 선택 -->')
    while (select != 'X' and select != 'x') :
        if (select == 'I' or select == 'i') :
            data = input('입력할 데이터 -->')
            push(data)
            print('스택 상태 : ',stack)
        elif (select == 'E' or select == 'e') :
            data = pop()
            print('추출된 데이터 -->',data)
            print('스택 상태 : ',stack)
        elif (select == 'V' or select == 'v') :
            data = peek()
            print('확인된 데이터 -->', data)
            print('스택 상태 : ', stack)
        else:
            print('입력이 잘못됨!')
        select = input('삽입(I)/추출(E)/확인(V)/종료(X) 중 하나 선택 -->')
    print('프로그램 종료!')
