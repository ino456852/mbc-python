s = set([1,2,3,1,3,1,3]) 
print(s) # {1, 2, 3}  중복 허용 안함

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print("교집합 s1 & s2 = ",s1 & s2) # 교집합
print("교집합 s1.intersection(s2) = ",s1.intersection(s2)) # 교집합

print("합집합 s1 | s2 = ",s1 | s2) # 합집합
print("합집합 1.union(s2) = ",s1.union(s2)) # 합집합

print("차집합 s1 - s2 = ",s1 - s2) # 차집합
print("차집합 s1.difference(s2) = ",s1.difference(s2)) # 차집합


# add() : 집합에 원소 추가
s1 = set([1, 2, 3])
s1.add(4)
print(s1)

# remove() : 집합에서 원소 제거
s1 = set([1, 2, 3])
s1.remove(2)
print(s1)

# update() : 집합에 여러 원소 추가
s1 = set([1, 2, 3])
s1.update([4, 5])
print(s1)