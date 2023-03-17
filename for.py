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

# 1から数えて逆数の和が8を越えるのはいくつか
reciprocal_ans = 0
reciprocal_n = 0
while reciprocal_ans < 8:  # これを越える値
    reciprocal_n += 1
    reciprocal_ans += 1/reciprocal_n
print(reciprocal_n)  # めっちゃ大きい
print(reciprocal_ans)  # ちょっと値を越える
print(reciprocal_ans - 1 / (reciprocal_n))  # ギリギリ超えない

# 1から数えて逆数の和が8を越えるのはいくつか
ans = 0
n = 0
while ans < 1000:  # これを越える値
    n += 1
    ans += n
print(n)  # めっちゃ大きい
print(ans)  # ちょっと値を越える
print(ans - n)  # ギリギリ超えない
