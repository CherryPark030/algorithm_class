##함수 선언부
def add_data(freind):
    katok.append(None)
    k_len = len(katok)
    katok[k_len - 1] = freind

def insert_data(n, freind):
    katok.append(None)
    k_len = len(katok)
    for i in range(k_len-1, n, -1):
        katok[i] = katok[i - 1]
        katok[i - 1] = None

    katok[n] = freind

def delet_data(position):
    katok[position] = None
    k_len = len(katok)
    for i in range(position + 1, k_len, 1):
        katok[i-1] = katok[i]
        katok[i] = None
    del katok[k_len -1]
    

##전역 변수부
katok = []

##메인 코드 
add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')
print(katok)

# #까톡,, 모모에게 처음으로 문자가 1회 옴
# add_data('모모')
# print(katok)

#2등 자리에 '솔라'를 삽입하기
insert_data(2, '솔라')
print(katok)

#2등자리 지우기
delet_data(2)
print(katok)
