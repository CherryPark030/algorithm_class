## 클래스 함수 선언 부분
class Node() :
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start) : #매개변수로 시작 노드 전달받음, start 노드부터 끝까지 출력
    current = start  #전달 받은 시작 노드를 현재 노드로 지정
    print(current.data, end=' ') #현재 노드 data 출력
    while (current.link != None): #현재 노드의 링크가 Nonde이 아닐떄까지 반복
        current = current.link #링크를 하나씩 타고 이동하며 
        print(current.data, end=' ') #데이터를 출력하는 함수
    print()

def insertNode(findData, insertData) :
    global memory, head, current, pre #global 전역변수 사용 -> 
    # Case 1 : 찾을 데이터가 맨 앞인 경우 (다현, 화사)
    if (findData == head.data) :
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        memory.append(node)
        return
    # Case 2 : 찾을 데이터가 중간 노드인 경우 (사나, 솔라)
    current = head
    while (current.link != None) :
        pre = current
        current = current.link
        if (current.data == findData) :
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            memory.append(node)
            return
    # Case 3 : 찾는 데이터가 없을 경우. 마지막에 추가(재남, 문별)
    node = Node()
    node.data = insertData
    current.link = node
    memory.append(node)
    return

def deleteNode(deleteData) :
    global memory, head, current, pre
    # Case 1: 삭제할 데이터가 head인 경우 (다현)
    if (deleteData == head.data) :
        current = head
        head = head.link
        del(current)
        return
    # Case 2: 삭제할 데이터가 중간인 경우 (쯔위)
    current = head
    while (current.link != None) :
        pre = current
        current = current.link
        if (current.data == deleteData) :
            pre.link = current.link
            del (current)
            return
    # Case 3: 없는 데이터를 삭제할 때 (재남)
    return

def findNode(findData) :
    global memory, head, current, pre
    current = head
    if (current.data == findData) :
        return current
    while (current.link != None) :
        current = current.link
        if (current.data == findData) :
            return  current
    return Node()

## 전역
memory = [] #생성할 노드를 저장할 메모르 준비
head, current, pre = None, None, None #시작, 현재, 이전 노드에 사용할 변수 준비
dataAry = ['다현', '정연', '쯔위', '사나', '지효'] # 자신의 데이터들....

## 메인
##  연결 리스트 생성(첫 노드)
node = Node() #첫 번째 노드 생성
node.data = dataAry[0] #노드에 데이터 입력
head = node #첫번째 노드를 헤드로 지정
memory.append(node) #생성된 노드 메모리에 저장

##  연결 리스트 생성(두번째 ~~)
for data in dataAry[1:] : # ['정연', '쯔위', ....
    pre = node # 현재 노드를 이전 노드로 저장함
    node = Node() #새로운 노드 생성
    node.data = data #노드에 data 입력
    pre.link = node #이전 노드와 생성된 노드 연결
    memory.append(node) #생성된 노드 메모리에 넣음

printNodes(head) #생성이 완료된 단순 연결 리스트 출력

## 데이터 삽입
# insertNode('다현', '화사')
# printNodes(head)
# insertNode('사나', '솔라')
# printNodes(head)
# insertNode('재남', '문별')
# printNodes(head)

# deleteNode('다현')
# printNodes(head)
# deleteNode('쯔위')
# printNodes(head)

fNode = findNode('사나')
print(fNode.data, '뮤직 비디오가 나옵니다')
​