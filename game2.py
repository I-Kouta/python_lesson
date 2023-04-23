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
print("\n")
# リストの重複を削除する
# list:ただの集合をリストに変換
# set:重複している要素を削除


def remove_duplicates(numbers):
    unique_numbers = list(set(numbers))
    print(f"{numbers}から重複を除いた結果は{unique_numbers}です")


remove_duplicates([5, 4, 3, 2, 1, 2, 3, 4, 5])
print("\n")
# 指定した文字列を取り除く・置き換える


def remove_string(s, target):
    new_s = s.replace(target, "")  # ""内の文字に置き換える
    print(f"{s}から{target}を取り除いた結果は{new_s}です")


remove_string("safari", "a")
print("\n")
# 要素を逆順にする(文字列も可)


def reverse_list(numbers):
    reverse_numbers = numbers[::-1]
    print(f"{numbers}を逆順にすると{reverse_numbers}です")


reverse_list([1, 2, 3, 4, 5])
# 辞書型データをソートする
