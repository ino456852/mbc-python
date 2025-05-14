# 난수 생성
import random
# print(random.randint(1, 100)) # 1부터 100까지의 난수 생성  

# 리스트 생성
numbers = []  # 빈 리스트 생성
numbers.append(random.randint(1,45)) # 1부터 45까지의 난수 생성
numbers.append(random.randint(1,45)) # 1부터 45까지의 난수 생성
numbers.append(random.randint(1,45)) # 1부터 45까지의 난수 생성
numbers.append(random.randint(1,45)) # 1부터 45까지의 난수 생성
numbers.append(random.randint(1,45)) # 1부터 45까지의 난수 생성
numbers.append(random.randint(1,45)) # 1부터 45까지의 난수 생성
numbers.sort() # 오름차순 정렬
print(numbers) # 숫자 중복 발생


# 중복된 숫자가 있을 경우 다시 생성
while len(numbers) < 6: # 6개 숫자가 될 때까지 반복
    num = random.randint(1, 45) # 1부터 45까지의 난수 생성
    if num not in numbers: # 중복 체크
        numbers.append(num) # 중복되지 않으면 리스트에 추가
        
a = [1, 2, 3, 4, 5]
# a.insert[0,100] # 오류 발생
a.insert(0, 100) # [100, 1, 2, 3, 4, 5] # 0번째 인덱스에 100 삽입
print(a)

#중복되지않는 로또번호 생성
a=range(1,5) # 마지막-1까지 연속 숫자. 1,2,3,4
print(list(a)) #[1, 2, 3, 4]
a=list(range(1,46)) #1~45까지 연속숫자
numbers = []
r = a.pop(random.randint(0,44))
numbers.append( r )
r = a.pop(random.randint(0,43))
numbers.append( r )
r = a.pop(random.randint(0,42))
numbers.append( r )
r = a.pop(random.randint(0,41))
numbers.append( r )
r = a.pop(random.randint(0,40))
numbers.append( r )
r = a.pop(random.randint(0,39))
numbers.append( r )
numbers.sort()
print(numbers)

# 간단한 로또번호 생성
a=list(range(1,46)) #1~45까지 연속숫자
b = random.sample(a, 6) # a에서 중복안되는 6개 추출
b.sort()
print(b)