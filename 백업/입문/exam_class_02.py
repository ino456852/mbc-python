def add(self, a, b): # 일반 함수는 self 필요없음
    return a+b
    
class FourCalc:
    def add(self, a, b): # 자신을 가리키는 self
        return a+b
    
    def sub(self, a, b):
        return a-b

c = FourCalc() #FourCalc 객체 생성
r = c.add(3,4) #-1
print(r)

r = c.sub(3,4)
print(r)