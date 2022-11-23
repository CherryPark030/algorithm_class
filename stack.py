###함수부


###변수부
stack = [None, None, None, None, None]
top = -1



###메인코드
#push()
top += 1
stack[top] = '커피'

top += 1
stack[top] = '녹차'

top += 1
stack[top] = '꿀물'

print('바닥:', stack)


#pop()
data = stack[top] #pop하는 것 data에 우선 저장
stack[top] = None
top -= 1

data = stack[top]
stack[top] = None
top -= 1

data = stack[top]
stack[top] = None
top -= 1
print('pop', data)