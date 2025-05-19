import time
import threading

# 숫자 출력
def print_num():
    for i in range(1000):
        time.sleep(0.5)
        print("Number %s\n" % i)
# 문자 출력
def print_char():
    for i in range(1000):
        time.sleep(0.5)
        c = chr(ord("가")+i)
        print("Char %s\n" % c)

# 동시 실행
t1 = threading.Thread(target=print_num)
t2 = threading.Thread(target=print_char)
t1.start()
t2.start()
print("Working")