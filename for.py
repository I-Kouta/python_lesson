# 繰り返し処理
num = 1
sum = 0
last = 80
print(str(num) + "から" + str(last) + "までの総和を算出")
while num <= last:  # いくつまで
    sum += num**4  # 何を足すか
    num += 1
print(sum)

print("end")
