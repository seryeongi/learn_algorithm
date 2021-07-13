## 함수 선언부 (클래스 선언)
def add_data(friend):
    katok.append(None)
    kLen = len(katok)
    katok[kLen-1] = friend

def insert_data(position, friend):
    katok.append(None)
    kLen = len(katok)

    for i in range(kLen-1, position, -1):
        katok[i] = katok[i-1]
        katok[i-1] = None

    katok[position] = friend

def delete_data(position):
    kLen = len(katok)

    for i in range(position,kLen-1,1):
        katok[i-1] = katok[i]
        katok[i] = None
    del(katok[kLen-1])

## 전역 변수부
katok = []
select = -1 # 1.추가 2.삽입 3.삭제 4.종료

## 메인 코드부
if __name__ == '__main__': # 메인 함수(진입점)
    while (select != 4):
        select = int(input('1.추가 2.삽입 3.삭제 4.종료 -->'))
        if (select == 1):
            data = input('추가 데이터-->')
            add_data(data)
            print(katok)
        elif (select == 2):
            pos = int(input('삽입 위치-->'))
            data = input('삽입 데이터-->')
            insert_data(pos,data)
            print(katok)
        elif (select == 3):
            pos = int(input('제거 위치-->'))
            delete_data(pos)
            print(katok)
        elif (select == 4):
            print(katok)
            exit
        else:
            print('1~4 중 하나를 입력하세요')
            continue
