info = []
print("이름을입력하세요:")
name = input()

print("나이를 입력하세요:")
age = int(input())

print("키를 입력하세요")
height = int(input())
if age >= 20 and height >= 160:
    info.append((name,age,height))
    print(f"{name}님은 입장 가능합니다")
else:
    print("입장불가")

from re import split




print("이름 입력:")
name_input = input()
name = name_input.split(",")

print("전화번호 입력:")
tel_input = input()
tel = tel_input.split(",")

result = []
for i in range(len(name)):
    result.append(f"{name[i]}:{tel[i]}")

print(", ".join(result))
