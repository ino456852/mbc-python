# f = open("./새파일.txt", 'w') 파일 만들기 없으면 생성 있으면 내용 삭제
# f.close()

# f = open("./새파일.txt", 'w')
# for i in range(1, 11):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()

# f = open("./새파일.txt", 'r')
# line = f.readline() # 한 줄 씩 읽기
# print(line)
# f.close()


# readline_all.py
# f = open("./새파일.txt", 'r')
# while True:
#     line = f.readline()
#     if not line: break
#     print(line)
# f.close()


# readlines.py
# f = open("./새파일.txt", 'r')
# lines = f.readlines()
# for line in lines:
#     print(line.strip()) # 양쪽 공백제거
# f.close()
# print("줄갯수 = ",len( lines),"개")


# read_for.py
# f = open("./새파일.txt", 'r')
# for line in f:
#     print(line.strip())
# f.close()

# add_data.py
# f = open("./새파일.txt",'a') # 텍스트 추가
# for i in range(11, 20):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()

# file_with.py
with open("foo.txt", "w") as f: # 자동 f.close()
    f.write("Life is too short, you need python")
