# import datetime
# day1 = datetime.date(1996, 10, 2)
# day2 = datetime.date(2021, 12, 24)
# diff = day2 - day1
# print(diff.days)

# day = datetime.date(2025, 5, 16)
# ds = "월,화.수,목,금,토,일".split(",")
# print(day.weekday())
# print(ds[day.weekday()-1])

# import time
# t = time.localtime(time.time())
# print(t)

# import glob
# for g in glob.glob("c:/*"):
#     print(g)

# import pickle
# f = open("test.txt", 'wb')
# data = {1: 'python', 2: 'you need'}
# pickle.dump(data, f)
# f.close()
import pickle
f = open("test.txt", 'rb')
data = pickle.load(f)
print(data)