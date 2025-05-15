# test_list = ['one', 'two', 'three']
# for i in test_list: 
#     print(i) 

# #
# d = "PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked"
# for k in d.split(","):
#     print(k)
    
# #
# a = [(1,2), (3,4), (5,6)] # first에 첫번째 값,last에 두번째 값
# for (first,last) in a:
#     print(first+last)

# #
# m = {"홍":1000, "김":1000, "박":1000}
# print("회비 납부자 목록:", m.keys())
# for n in m.keys():
#     print("납부 회원 이름:",n)
#     print(f"{n}이 납부한 금액={m[n]}")
    
# #
# print( list(range(30)))
# print( list(range(1,5))) #1포함 5미만

# for i in range(2,10):        # 1번 for문
#     s = " "
#     for j in range(1, 10):   # 2번 for문
#         s += str(i*j)+" " 
#     s += "\n"
# print(s) 

# 로또번호 6개씩 5번 출력하세요
# 형식: 2,3,4,5,6
# import random
# for _ in range(5): 
#     r = random.sample(range(1,46),6)
#     r = [ str(i) for i in r] # 컴프리핸션
#     print(",".join(r)) # r을 str로 변환해서 오류 안남
#     # nums = random.sample(range(1,46),6)
#     # print(nums)

# #
# a = [1,2,3,4]
# result = [num * 3 for num in a if num % 2 == 0]
# print(result)

result = [x*y for x in range(2,10)
              for y in range(1,10)]
print(result)