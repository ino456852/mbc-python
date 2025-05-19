class CarExpenseBook:
    def __init__(self):
        self.booklist = []
    
    def add_expense(self, date, category, amount, description=""):
        book={
            "date":date, 
            "category":category, 
            "amount":amount, 
            "description":description
        }
        self.booklist.append(book)
        
    def show_all(self):
        for b in self.booklist:
            print(b)
    
    def total_expense(self):
        return sum([  b["amount"] for b in self.booklist ])
        # total = 0
        # for b in self.booklist:
        #     total += b["amount"]
        # return total
    
    def total_by_category(self,category):
        return sum([  b["amount"] for b in self.booklist if b["category"]==category ])
        # total = 0
        # for b in self.booklist:
        #     if b["category"]==category:
        #         total += b["amount"]
        # return total
        
    def save(self):
        import pickle
        f = open("car_ex.pickle", 'wb')
        pickle.dump(self.booklist, f)
        f.close()
    
    def load(self):
        import pickle
        f = open("car_ex.pickle", 'rb')
        self.booklist = pickle.load(f)
        f.close()

if __name__ == "__main__":
    book = CarExpenseBook()

    # book.add_expense("2025-05-01", "주유", 60000, "셀프주유")
    # book.add_expense("2025-05-03", "세차", 8000)
    # book.add_expense("2025-05-07", "정비", 150000, "엔진오일 교환")

    # book.show_all()

    # print("총 지출:", book.total_expense())
    # print("주유 지출:", book.total_by_category(""))
    # book.save() # 파일에 저장
    
    # book = CarExpenseBook()
    book.load()
    book.show_all()