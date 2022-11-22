##함수 선언 부분
def add_data(friend):
    katok.append(None)
    katok[-1] = friend
    print(katok)

def insert_data(position, friend):
    katok.append(None)
    k_len = len(katok)
    for i in range(k_len-1, position, -1):
        katok[i] = katok[i-1]
        katok[i-i] = None
    katok[position] = friend
    print(katok)

def delete(position):
    katok[position] = None
    k_len = len(katok)
    for i in range(position, k_len-1, 1):
        k[i] = k[i+1]
        k[i+1] = None
    print(katok)



##전역
katok=[]
select = -1 #1:추가, 2: 삽입, 3: 삭제, 4: 종료

# ##메인

while True:
    select = int(input('1: 추가, 2: 삽입, 3: 삭제, 4: 종료 중 하나를 입력하시오'))
    if select == 1:
        friend = input('친구 이름을 입력하세요 :')
        add_data(friend)
    elif select == 2:
        position = int(input("위치를 입력하세요 :"))
        friend = input("친구 이름을 입력하세요 :")
        insert_data(position, friend)
    elif select == 3:
        postion = int(input("위치를 입력하세요 :"))
        delete_data(position)
    else: 
        print('종료합니다.')
        break
