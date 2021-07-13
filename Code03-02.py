katok = ['다현', '정연', '쯔위', '사나', '지효']

def insert_data(position, friend):
    katok.append(None)
    #전체길이파악은 기본
    kLen = len(katok)

    for i in range(kLen-1,position,-1):
        katok[i] = katok[i-1]
        katok[i-1] = None

    katok[position] = friend

print(katok)
insert_data(2,'솔라')
print(katok)
insert_data(6,'문별')
print(katok)
