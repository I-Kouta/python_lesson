# 文字列の出現回数をカウントする
def count_occurrences(string, target):
    count = 0
    # 文字列をループさせて出現した回数を数える
    for char in string:
        if char == target:
            count += 1
    if count == 0:
        print(f"{string}に{target}は含まれていません")
    else:
        print(f"{string}に{target}は{count}つ含まれます")


count_occurrences("perfume", "e")

# 指定した文字列を取り除く
# 文字列の重複を削除する
# 要素を逆順にする
# 文字列を反転させる
# 辞書型データをソートする
