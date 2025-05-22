def calc():
    total = 0 # 지역
    
    def add(a=0):
        nonlocal total # 지역변수 total
        total = total + a
    

    def get_total():
        return total
    return add, get_total

add, get_total = calc()
add(1)
add(2)
add(3)
print(get_total())