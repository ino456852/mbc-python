class CarExpenseBook:
    def __init__(self):
        # 모든 지출을 저장할 리스트
        self.expenses = []

    def add_expense(self, date, category, amount, description="주유"):
        # 한 건의 지출 정보를 딕셔너리로 만듦
        expense = {
            "date": date,             # 날짜
            "category": category,     # 분류 (주유, 세차 등)
            "amount": amount,         # 금액
            "description": description  # 설명 (기본은 "주유")
        }
        # 리스트에 추가
        self.expenses.append(expense)

    def total_expense(self):
        # 총 지출 금액 계산
        total = 0
        for e in self.expenses:
            total += e["amount"]
        return total

    def total_by_category(self, category):
        # 특정 분류(예: 주유)의 총 지출 계산
        total = 0
        for e in self.expenses:
            if e["category"] == category:
                total += e["amount"]
        return total

    def show_all(self):
        # 전체 지출 내역 출력
        for e in self.expenses:
            print(e)

if __name__ == "__main__":
    book = CarExpenseBook()

    book.add_expense("2025-05-01", "주유", 60000, "셀프주유")
    book.add_expense("2025-05-03", "세차", 8000)
    book.add_expense("2025-05-07", "정비", 150000, "엔진오일 교환")

    book.show_all()

    print("총 지출:", book.total_expense())
    print("주유 지출:", book.total_by_category(""))
