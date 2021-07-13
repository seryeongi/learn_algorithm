katok = [] # 빈 배열
# 친구를 카톡 리스트에 넘겨주는 함수
def add_data(friend):
    katok.append(None) # 친구가 들어갈 빈 칸 만들기 (0번째 칸)
    kLen = len(katok) # 1
    katok[kLen-1] = friend # 맨 마지막번째

add_data('다현');
add_data('정연');
add_data('쯔위');
add_data('사나');
add_data('지효');
add_data('모모');
print(katok);
