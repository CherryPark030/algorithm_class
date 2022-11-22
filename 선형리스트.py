##함수 선언부



##전역 변수부
katok = ['다현', '정연', '쯔위', '사나', '지효']


##메인 코드부
print(katok)


##카톡.. 모모에게 처음으로 문자가 1회 옴
katok.append(None)
##빈칸에 새 친구 넣기
katok[5] = '모모'

##데이터 삽입
##까톡,, 40번 연속으로 미나에게 문자가 옴
##빈칸 하나 추가
katok.append(None)
##3등 자리까지 한칸씩 옆으로 밀기 (등수를 낮춤)
katok[6] = katok[5]
katok[5] = None

katok[5] = katok[4]
katok[4] = None

katok[4] = katok[3]
katok[3] = None

katok[3] = '미나'

###사나 삭제하기
#사나 자리 비우기
katok[4] = None

#한칸씩 등수 올리기
katok[4] = katok[5]
katok[5] = None

katok[5] = katok[6]
katok[6] = None

del katok[6]


##출력
print(katok)