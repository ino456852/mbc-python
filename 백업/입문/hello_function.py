# # def add(a, b): # 매개변수
# #     return a+b
# # print( add(a = 3, b = 4)) # 인수


# # def add_many(*args): 
# #     result = 0 
# #     for i in args: 
# #         result = result + i   # *args에 입력받은 모든 값을 더한다.
# #     return result 

# # r = add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# # print(r)

# # r = add_many(1, 2, 3)
# # print(r)

# # # 매개변수 없고 리턴값 있는것
# # # def hi():
# # #     print("Hi")
# # # print(hi())

# # #
# # def sub(a, b):
# #     return a - b

# # result = sub(a=7,b=3) # a에 7,b에 3을 전달
# # print(result)

# # result = sub(b=3,a=7) # a에 7,b에 3을 전달
# # print(result)


# # # 
# # def add_mul(choice, *args): 
# #     if choice == "add":   # 매개변수 choice에 "add"를 입력받았을 때
# #         result = 0 
# #         for i in args: 
# #             result = result + i 
# #     elif choice == "mul":   # 매개변수 choice에 "mul"을 입력받았을 때
# #         result = 1 
# #         for i in args: 
# #             result = result * i 
# #     return result 


# # result = add_mul('add', 1,2,3,4,5)
# # print(result)

# # result = add_mul('mul', 1,2,3,4,5)
# # print(result)
# # #
# # a,b = (3,4)
# # print(a,b)
# # b,a = (a,b)
# # print(a,b)

# # def add_and_mul(a,b): 
# #     return a+b, a*b
# # r1, r2 = add_and_mul(3,4)
# # print(r1, )


# # default1.py
# def say_myself(name, age, man=True): 
#     print("나의 이름은 %s 입니다." % name) 
#     print("나이는 %d살입니다." % age) 
#     if man: 
#         print("남자입니다.")
#     else: 
#         print("여자입니다.")

# print(say_myself("홍길동",25))
# print(say_myself("홍길동",25,False))

# # show_gugudan(3) # 3단 구구단
# # show_gugudan(4, 5, 6) # 4,5,6 단 구구단


# # vartest.py
# a = 1
# def vartest():
#     global a
#     a = a + 1

# vartest()
# print(a)

# add = lambda a,b : a+b # lambda 한줄함수, def 생략
# result = add(3,4)
# print(result)

# number = input("숫자를 입력하세요: ")
# print( type(number))
# n = int(number)
# print(n*100)
print(1,2,3,sep="-")