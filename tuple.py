# タプル作成
x = 3
y = 4
z = 2
numTuple = (x, y, z)
print(numTuple)
# 要素を取得
print(str(numTuple[0]) + " + " + str(numTuple[1]) + " + " +
      str(numTuple[2]) + " = " + str(numTuple[0] + numTuple[1] + numTuple[2]))
print(str(numTuple[0]) + " × " + str(numTuple[1]) + " × " +
      str(numTuple[2]) + " = " + str(numTuple[0] * numTuple[1] * numTuple[2]))
# 要素数の取得
print("要素数は" + str(len(numTuple)) + "つです")
print(str(len(numTuple)) + "つ数値の積は" +
      str(numTuple[0] * numTuple[1] * numTuple[2]) + "です")
