# # 리스트에 저장
# todo = ["공과금내기","2025-05-20","진행중"]
# print(todo)
# print("할일내용 : ",todo[0]) 
# print("기한날짜 : ",todo[1]) # 각 인덱스를 기억해야함

# 할일을 사전타입에 저장
# todo = {
#     "title":"공과금내기",
#     "duoDate":"2025-09-20",
#     "status":"진행중"
# }
# print("할일내용 : ",todo["title"]) # 알아보기 쉬움
# print("할일내용 : ",todo["duoDate"])

# # 1 할일을 여러개저장
# todolist = []
# todolist.append({
#     "title":"공과금내기",
#     "duoDate":"2025-09-20",
#     "status":"진행중"
# })
# # 2
# todolist = []
# todolist.append(todo)
# todo = {
#     "title":"파이썬공부",
#     "duoDate":"2025-09-20",
#     "status":"기한초과"
# }

# todolist.append(todo)
# print(f"저장갯수: {len(todolist)}")

# 이상적인 사용형태
# todo = TodoApp() # 할일 관리 객체
# showMenu()
# todo.insert( title = "", dueDate="", status="") #할일 등록
# todo.list() # 할일 목록 출력
# todo.findTodo(no=2)
# todo.update(no=2, title="", tueDate="", status="")
# todo.delete(no=2)
# todo.count() #등록된 할일 갯수