treeHit = 0
while treeHit < 10:
    treeHit = treeHit +1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")

# 로또번호 생성코드
import random
count = 0
numbers = []
while count < 6:
    r = random.randint(1,45)
    numbers.append(r)
    count += 1
print(numbers)

coffee = 10 
money = 300
while money: 
    print("돈을 받았으니 커피를 줍니다.") 
    coffee = coffee -1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

a = 0 # 
while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a)

