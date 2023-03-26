# リストを作成する
PerfumeList = ["Pick Me Up", "Spinning World", "コミュニケーション", "FAKE IT"]
print(PerfumeList[0])  # Pick Me Up
print(PerfumeList[-1])  # FAKE IT
print(PerfumeList[-2])  # コミュニケーション
print("最後の要素は" + PerfumeList[len(PerfumeList) - 1])
print("要素の数は" + str(len(PerfumeList)) + "つです\n")

# スライス機能
print(PerfumeList[0:2])  # SWまで。最後は要素+1
print(PerfumeList[:2])  # 同じ
print(PerfumeList[2:])
print("\n")
print("変更前のオブジェクトidは" + str(id(PerfumeList)))
# 要素を入れ替える
PerfumeList[-1] = "マワルカガミ"
print(PerfumeList[-1])  # マワルカガミ
print("変更後のオブジェクトidは" + str(id(PerfumeList)) + "で、変わっていません")
print("\n")
# リストを追加する
PerfumeList.append("ハテナビト")
print(PerfumeList)
print("\n")
# 指定位置に要素を挿入
numberList = [101, 102, 106, 107]
numberList.insert(2, 103)  # 2番目の値の前に3を挿入する
print(numberList)  # 101, 102, 103, 106, 107
addList = [104, 105]
numberList[3:3] = addList
print(numberList)  # これで番号順
del numberList[-1]
print(numberList)  # 107が消えている
del numberList[2:5]
print(numberList)  # 103から105が消えている
numberList.pop(1)
print(numberList)  # 102が消えている
numberList.remove(101)  # "101"は不可
print(numberList)  # 101が消えている
numberList.clear()  # 全ての要素を削除
print(numberList)  # []のみ
