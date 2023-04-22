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

# リストの重複を削除する
# list:ただの集合をリストに変換
# set:重複している要素を削除


def remove_duplicates(numbers):
    unique_numbers = list(set(numbers))
    print(f"{numbers}から重複を除いた結果は{unique_numbers}です")


remove_duplicates([5, 4, 3, 2, 1, 2, 3, 4, 5])
# 指定した文字列を取り除く
# 要素を逆順にする
# 文字列を反転させる
# 辞書型データをソートする
