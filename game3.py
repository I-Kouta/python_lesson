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
