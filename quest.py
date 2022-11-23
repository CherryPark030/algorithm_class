#2차원 배열 처리


#5*5  2차원 배열을 생성 (모두 0) 후, 값을 3의 배수로 채우기
ary2 = [[0 for _ in range(5)] for _ in range(5)]

num = 3
for i in range(5):
    for k in range(5):
        ary2[i][k] = num
        num += 3

for i in range(5):
    for k in range(5):
        print(ary2[i][k], end=' ')
    print()