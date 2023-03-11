# 数値
print(3.34e+2)  # 334.0

print('12 × 12 =' + str(12 * 12))  # 12 × 12 = 144
print('100 ÷ 3 =' + str(100 / 3))  # 100 ÷ 3 = 33.333333…
print('100 ÷ 3 =' + str(100 // 3))  # 100 ÷ 3 = 33
print('100を3で割ったあまりは' + str(100 % 3))  # 余り1
print('32の2乗は' + str(32 ** 2))  # 1024,累乗の計算
print("\n")
# ビット値
num = 10
bin_str = format(num, 'b')
print(str(num) + 'は2進数では' + bin_str)
print("10 | 12 =" + str(10 | 12))
