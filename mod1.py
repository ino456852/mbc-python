# mod1.py
def add(a, b):
    return a + b

def sub(a, b): 
    return a-b

if __name__ == "__main__":
    # 직접실행시키는 경우
    print("mod1.py의 name=",__name__)
    print(add(1,4))
    print(sub(4,2))