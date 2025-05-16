from exam_class_05 import *
book = CarExpenseBook()
book.add_expense("2025-05-01", "주유", 60000, "셀프주유")
book.add_expense("2025-05-03", "세차", 8000)
book.add_expense("2025-05-07", "정비", 150000, "엔진오일 교환")
book.show_all()