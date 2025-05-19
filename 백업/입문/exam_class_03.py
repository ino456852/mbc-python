class FourCalc:
    def __init__(self, a, b): # 생성자?
        self.a = a
        self.b = b
    
    def setData(self, a, b):
        self.a = a
        self.b = b
    
    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b
    
c = FourCalc(3,4)
r = c.add(); print(r)
r = c.sub(); print(r)

c.setData(5,7)
r = c.add(); print(r)

class MoreFoueCalc(FourCalc):
    def pow(self):
        result = self.a ** self.b
        return result

print("** MoreFoueCalc **")
c = MoreFoueCalc(3,4)
r = c.add(); print(r)
r = c.sub(); print(r)

c.setData(5,2)
r = c.add(); print(r)
r = c.pow(); print(r)
