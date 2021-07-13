SIZE = 5
stack = [None for _ in range(SIZE)]
top = -1

top += 1
stack[top] = '커피'
top += 1
stack[top] = '녹차'
top += 1
stack[top] = '꿀물'
print(stack)

data = stack[top]
stack[top] = None
top -= 1
print('추출-->', data)

data = stack[top]
stack[top] = None
top -= 1
print('추출-->', data)
