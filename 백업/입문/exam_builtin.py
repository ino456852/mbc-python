# 내장함수
# import mod1
# print(dir(mod1))

# for r in dir(mod1):
#     print(r)
# diff = ord("날") - ord("가")
# print(diff)
# print(diff/588)
# 회원목록
# 납부회비 목록
# mens = "홍,김,박".split(",") #["홍","김","박"]
# moneys = "1000,2000,3000".split(",")
# mm = list(zip(mens,moneys))
# print(mm)

# import os
# print(os.environ['PATH'])
# print(os.getcwd())
# f = os.popen("dir")
# print(f.read())

# zipfile_test.py
# import zipfile

# 파일 합치기
# with zipfile.ZipFile('mytext.zip', 'w') as myzip:
#     myzip.write('exam_class_01.py')
#     myzip.write('exam_class_02.py')
#     myzip.write('exam_class_03.py')

# 해제하기
# with zipfile.ZipFile('mytext.zip') as myzip:
#     myzip.extractall()

