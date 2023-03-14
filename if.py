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
print("Perfume Locksといえば" + PerfumeLocks + "!!!")
