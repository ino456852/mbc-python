a = "20230331Rainy"
print(a[:8]) # 0~7
print(a[8:]) # 8~끝
print(a[8:10]) # 8~9


a = "age = %d" % 30
print(a)

a = "%d * %d = %d" % (3, 4, 3*4)
print(a)

a = "%10s" % "hello" # 우측 정렬
print(a)

a = "%-10shi" % "hello" # 좌측 정렬
print(a)

name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')
print('나의 이름은 %s입니다. 나이는 %d입니다.' % (name, age))
print('나의 이름은 {}입니다. 나이는 {}입니다.'.format(name, age)) # 거의 안씀
a = "Pytion"*2
print(a.count('n'))

a = "Python is the best choice"
print(a.find('b')) # 14
print(a.find('f')) # -1
print(",".join('abcd')) # a,b,c,d
print("-".join('abcd')) # a-b-c-d
print( ",".join(['a', 'b', 'c', 'd'])) # 배열 
# print( ",".join((100,200))]) # 오류발생
# print("A" + 100) # 오류발생 문자열 + 숫자 => 타입이 달라 연산오류
print("100" + str(100)) # 100100
print(int(100) + 100) # 200

a = "PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked"
arr = a.split(",")
print(arr) # ['PassengerId', 'Survived', 'Pclass', 'Name',sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
print(arr[0]) # PassengerId
print(arr[1]) # Survived
print(arr[2]) # Pclass


# 문자열 관련 함수
s = "Python"
print(s.isalpha()) # True

s = "Python3"
print(s.isalpha()) # False

s = "Hello World"
print(s.isalpha()) # False



# 숫자 관련 함수
s = "12345"
print(s.isdigit()) # True

s = "1234a"
print(s.isdigit()) # False

s = "12 34" 
print(s.isdigit()) # False


# 특정 문자열로 시작하는지 확인
s = "Life is too short"
print(s.startswith("Life")) # True

# 특정 문자열로 끝나는지 확인
s = "Life is too short"
print(s.endswith("short")) # True

# 현재폴더내 파일목록
import os
file_list = os.listdir("./") # 현재폴더내 파일목록
print("현재 폴더 내 파일 갯수 = ",len(file_list)) 
print("현재 폴더 내 파일 갯수 = ",file_list) 
print(file_list[0].endswith("exe")) # 현재폴더내 첫번째 파일이 exe인지 확인