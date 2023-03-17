# 繰り返し処理
num = 1  # この値から
sum = 0
last = 80
print(str(num) + "から" + str(last) + "までの総和を算出")
while num <= last:  # いくつまで
    sum += num**4  # 右辺の処理をして繰り返す
    num += 1  # 1ずつ増やしていく
else:
    print("計算結果は" + str(sum) + "です")
