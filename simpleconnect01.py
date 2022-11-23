## 함수
class Node() : #Node 라는 데이터형을 만듦
    def __init__(self): #데이터형을 생성할 때 자동으로 실행되는 부분
        self.data = None #데이터 저장되는 부분
        self.link = None #링크 저장되는 부분

def printNodes(start) : # start 노드부터 끝까지 출력
    current = start
    print(current.data, end=' ') #current.data 출력
    while (current.link != None): #current.link가 None이 아니라면
        current = current.link #링크를 타고 current를 업데이트하면서
        print(current.data, end=' ') #끝까지 data를 출력함
    print()

def insertNode(findData, insertData): #삽입
    global memory, head, current, pre #
    #case 1 : 찾을 데이터가 맨 앞인 경우(다현, 화사)
    if (findData == head.data):
        node = Node() #빈 노드 생성
        node.data = insertData #빈 노드에 insertData 입력
        node.link = head #새로운 노드의 링크로 헤드가 가리키는 노드를 지정
        head = node #헤드 노드를 새 노드로 지정
        memory.append(node) #노드를 메모리에 넣음
        return
    #case 2 : 찾을 데이터가 중간 노드인 경우(사나, 솔라)
    current = head #헤드에서 시작해서 current가 findData인지 확인한다
    while (current.link != None) :
        current = current.link
        if (current.data == findData):
            node = Node() #빈노드 생성
            node.data = insertData #빈노드에 insertData 입력
            node.link = current #노드의 링크에 current 연결
            pre.link = node #current 이전의 노드의 링크와 새로운 노드 연결
            memory.append(node) #메모리에 노드를 넣음
            return

## 전역
memory = []
head, current, pre = None, None, None #head, current, pre를 위치를 임시로 저장하기 위한 저장공간이라고 생각
dataAry = ['다현', '정연', '쯔위', '사나', '지효'] # 자신의 데이터들....

## 메인
##  연결 리스트 생성(첫 노드)
node = Node()
node.data = dataAry[0]
head = node
memory.append(node)

##  연결 리스트 생성(두번째 ~~)
for data in dataAry[1:] : # ['정연', '쯔위', ....
    pre = node # 앞 노드를 잡고 있음.
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)

printNodes(head)