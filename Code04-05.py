## 함수, 클래스 선언부
class Node(): # 내가 지어준 이름
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start) : # 출력
    current = start
    print(current.data, end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()

def insert_node(findData, insertData) :
    global memory, head, current, pre
    # 예) 다현 앞에 화사를 삽입
    if head.data == findData : # 첫 노드를 삽입
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return

    current = head               # 중간 노드 삽입
    while current.link != None :
        pre = current
        current = current.link
        if current.data == findData :
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return

    node = Node()    # 마지막에 노드 삽입
    node.data = insertData
    current.link = node

def delete_node(deleteData) :
    global memory, head, current, pre

    if head.data == deleteData: # 첫 노드 삭제
        current = head
        head = head.link
        del(current)
        return

    current = head
    while current.link != None :
        pre = current
        current = current.link # 다음으로 가기
        if current.data == deleteData :
            pre.link = current.link
            del(current)
            return

def find_node(findData):
    global memory, head, current, pre
    current = head
    if current.data == findData :
        return current
    while current.link != None :
        current = current.link
        if current.data == findData :
            return current
    return Node() # 빈 노드 반환


## 전역 변수부
memory = []
head, current, pre = None, None, None
dataArray = ['다현', '정연', '쯔위', '사나', '지효'] # DB에서 읽기, 크롤링된 데이터

## 메인 코드부
# 첫 데이터 입력
node = Node() # node: 재활용해야해서
node.data = dataArray[0]
head = node
memory.append(node)

for data in dataArray[1:] : # 두번째부터 ['정연', ...]
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)

printNodes(head)

insert_node('다현', '화사')
printNodes(head)
insert_node('사나', '솔라')
printNodes(head)
insert_node('재남', '문별')
printNodes(head)

delete_node('화사')
printNodes(head)
delete_node('쯔위')
printNodes(head)
delete_node('문별')
printNodes(head)
delete_node('재남')
printNodes(head)

fNode = find_node('다현')
print(fNode.data)
fNode = find_node('지효')
print(fNode.data)
fNode = find_node('재남')
print(fNode.data)