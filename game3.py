# 階乗を行う
def factorial(n):
    if n <= 0:
        return 1
    else:
        return n * factorial(n - 1)


m = 5
resultFactorial = factorial(m)
if m <= 0:
    print(f"0以下の値が与えられています")
else:
    print(f"{m}の階乗は{resultFactorial}です")
# 文字列をアルファベット準にソート
strings = ["game", "cling cling", "Story", "fusion"]
sort_strings = sorted(strings, key=str.lower)  # key=str.lowerで大文字小文字を区別しない
print(sort_strings)


def sort_strings_case_insensitive(strings):
    print(sorted(strings, key=str.lower))


# 日本語は、平仮名→カタカナ→漢字の順
sort_strings_case_insensitive(["日本語", "アイスクリーム", "神奈川県", "いーぶい"])
