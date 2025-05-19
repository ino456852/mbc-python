class Family:
    lastname = "김"


print(Family.lastname)  # 김

a = Family()
print(a.lastname)  # 김

b = Family()
print(b.lastname)  # 김

a.lastname = "박"
print(a.lastname) # 박
print(b.lastname) # 김
print(Family.lastname) # 김