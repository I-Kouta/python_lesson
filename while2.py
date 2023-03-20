# for文を使った繰り返し
setList = ["edge", "Tiny Baby", "Hurly Burly"]
for list in setList:
    print(list)
else:
    print("\n")

count = 0
list = {"e": "edge", "T": "Tiny Baby", "H": "Hurly Burly"}
for initial, value in list.items():
    print("頭文字：" + initial + ",曲：" + value)
    count += 1
else:
    print("曲数：" + str(count))
