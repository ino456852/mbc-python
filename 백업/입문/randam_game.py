import random

com = random.randint(1, 100)
count = 0
while True:
    user = int(input("1~100 사이 숫자 입력: "))
    count += 1
    if user == com:
        print("정답입니다!")
        break
    
    elif user < com:
        print("숫자를 높여주세요.")
    else:
        print("숫자를 낮춰주세요.")
        
        
print(f"총 {count}번 만에 맞추셨습니다.")
