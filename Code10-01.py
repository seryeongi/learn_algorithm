def openBox() :
    global count
    print('박스 열기 ~~~')
    count -= 1
    if count == 0 :
        print('반지 넣기~~ 마이 프레셔스.')
        return
    openBox()
    print('박스 닫기!!!!')

count = 10
openBox()