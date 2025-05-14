dic = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(dic)
print("name = ", dic['name'])  # pey
print("phone = ", dic['phone'])  # 010-9999-1234
# print("myphone = ", dic['myphone'])  # 미등록 키 추출시 KeyError 발생

dic['phone'] = '010-1111-2222'  # 값이 있으면 수정
print("phone = ",dic['phone'])  # 010-1111-2222

dic['myphone'] = '010-3333-4444'  # 값이 없으면 추가
print("myphone = ", dic['myphone'])  # 010-3333-4444

# 삭제
del dic['myphone']  # myphone 키 삭제
print(dic)  # {'name': 'pey', 'phone': '010-1111-2222', 'birth': '1118'}

print(dic.keys())  # dict_keys(['name', 'phone', 'birth'])

# 반복문 
for k in dic.keys(): # 키만 출력
    print(k)  # name, phone, birth
    
for k in dic.values(): # 값만 출력
    print(k)  # name, phone, birth
    
for k, v in dic.items(): # 키와 값 모두 출력
    print(k, v)  # name pey, phone 010-1111-2222, birth 1118
    
# 딕셔너리 초기화
dic.clear()  # 모든 키와 값 삭제
print(dic)  # {}

# 회비입금내역
all_members = ["홍", "김", "박", "최" ,"강"]
m = {"홍":1000, "김":1000, "박":1111}
# 회비 납부자 목록
ma = m.keys()
print("회비 납부자 목록 = ", ma)  # 회비 납부자 목록 =  dict_keys(['홍', '김', '박'])
print("회비 미납부자 목록 = ", set(all_members) - set(ma))  # 회비 미납부자 목록
