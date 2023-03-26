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
PerfumeList[-1] = "マワルカガミ"
print(PerfumeList[-1])  # マワルカガミ
print("変更後のオブジェクトidは" + str(id(PerfumeList)) + "で、変わっていません")
