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
print("\n")
# 辞書型データをソートする


def sort_dictionary(d):
    sort_d = dict(sorted(d.items(), key=lambda x: x[1]))
    print(f"ソート前の辞書:{d}")
    print(f"値に基づいてソートされた辞書:{sort_d}")


sort_dictionary({"a": 2, "b": 1, "c": 3})
print("\n")
# フィボナッチ数列のn項目を求める
# 1から始まる場合(1, 1, 2, 3, 5, 8, 13, …)


def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


n = 9
sequence_sum = fibonacci(n)
print(f"1から始まるフィボナッチ数列の{n}番目の値は{sequence_sum}です")
print("\n")
# 0から始まる場合(0, 1, 1, 2, 3, 5, 8, 13, …),0項目は0


def fibonacci_zero(m):
    if m == 0:
        return 0
    elif m == 1:
        return 1
    else:
        return fibonacci(m - 2) + fibonacci(m - 1)


m = 0
sequence_sumM = fibonacci(m)
print(f"0から始まるフィボナッチ数列の{m}番目の値は{sequence_sumM}です")
# 整数が素数かどうか判別する
# 整数2つの最大公約数を求める
