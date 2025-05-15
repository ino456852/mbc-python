# if문
money = 2000
if money >= 3000:
    print("택시를 타고 가라")
    print("택시를 타고 가라")
else:
    print("걸어 가라")
    print("걸어 가라")

ma = ["홍","김"]
print ("김" in ma) # True
print ("이" in ma) # False
print ("이" not in ma) #True

# 가위바위보
import random
r = random.randint(1,3)
print(r)
if r == 1:
    print("가위")
elif r == 2:
    print("바위")
else:
    print("보")
    
#
gbb = ["가위","바위","보"]
r = random.randint(1,3)
print(gbb[r-1])

score = 90
message = "success" if score >= 60 else "failure"
print(message)

