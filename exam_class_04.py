class TodoApp():
    def __init__(self):
        self.todolist = []  # 빈리스트

    def insert(self, title, dueDate, status="진행중"):
        # PK값으로 시간의 밀리초를 사용
        import datetime
        now = datetime.datetime.now().timestamp()*100000  # 밀리초
        todo = {
            "no": int(now),
            "title": title,
            "dueDate": dueDate,
            "status": status
        }
        self.todolist.append(todo)

    def count(self):  # 할일 개수
        return len(self.todolist)

    def list(self):  # 목록 출력
        for td in self.todolist:
            print(td)

    def findTodo(self, no):
        for td in self.todolist:
            if td["no"] == no:
                return td
        return None


# 이상적인 사용형태
todo = TodoApp()  # 할일 관리 객체
# showMenu()
todo.insert(title="공과금내기", dueDate="2025-05-20")  # 할일 등록
todo.insert(title="파이썬공부", dueDate="2025-05-10", status="기한초과")  # 할일 등록
todo.list()  # 할일 목록 출력
no = input("찾을 할일번호 : ")
td = todo.findTodo(no=int(no))
print(td)
# todo.update(no=2, title="", tueDate="", status="")
# todo.delete(no=2)
print(todo.count())  # 등록된 할일 갯수


