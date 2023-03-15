# 条件分岐
music = "Spring of Life"
print("春の曲といえば" + music + " 派\n")

if music == "Spring of Life":
    print("サプライズを待っていてもしょうがないから〜")
else:
    print("ワンルーム・ディスコ派ですか？")
print("ドライブはFAKE IT派です")

likePerfume = "気になる姫"
if likePerfume == "こどものっち":  # ここは一致を確かめるので==
    PerfumeLocks = "こどものっち"  # ここは代入なので=
elif likePerfume == "かしゆかおじさん":
    PerfumeLocks = "かしゆかおじさん"
else:
    PerfumeLocks = "気になる姫"
print("Perfume Locksといえば" + PerfumeLocks + "!!!\n")
# 比較演算子
msgA = int(len("マワルカガミ"))  # 6
msgB = int(len("コミュニケーション"))  # 9
print(bool(msgA == msgB))  # false
print(bool(msgA != msgB))  # true
print(bool(msgA <= msgB))  # true
print('\n')
# unicodeのコードポイント
print(ord("a"))  # 97
print(ord("B"))  # 66
# 要素が含まれる
array = ["レーザービーム", "スパイス", "いじわるなハロー"]
print(bool("スパイス" in array))  # true
print(bool("ビーム" in array))  # false
