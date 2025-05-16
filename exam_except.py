try:
    f = open("foo.txt", 'r')
    print("파일오픈!")
    r = 4 / 0
    print("계산종료!")
    
except FileNotFoundError as e:
    print("파일 오픈 오류")
except ZeroDivisionError as e:
    print("0 나누기 오류")