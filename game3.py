# 階乗を行う
import locale
import unicodedata
locale.setlocale(locale.LC_COLLATE, 'ja_JP.UTF-8')


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

# 日本語は、平仮名→カタカナ→漢字の順
stringsB = ["日本語", "アイスクリーム", "神奈川県", "いーぶい"]


sort_stringsB = sorted(
    stringsB, key=lambda s: unicodedata.normalize('NFKC', s).lower())
print(sort_stringsB)
