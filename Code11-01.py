## 함수
def findMinIdx(ary) : # 배열의 최소 위치
    minIdx = 0
    for i in range(1, len(ary)) :
        if (ary[minIdx] > ary[i]) :
            minIdx = i
    return minIdx
## 변수
import random
before = [random.randint(100,999) for _ in range(8)]
after = []
## 메인
# testAry = [55 ,88, 33, 77]
# minPos = findMinIdx(testAry)
# print('최솟값 -->', testAry[minPos])
print('정렬 전 -->',before)
for i in range(len(before)) :
    minPos = findMinIdx(before)
    after.append(before[minPos])
    del (before[minPos])

print('정렬 후 -->',after)