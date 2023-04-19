# 1.リストの要素の平均値を求める
def mean(numbers):
    ave = sum(numbers) / len(numbers)
    num = len(numbers)
    print(f"{num}つの要素の平均値は{ave}です")


mean([1, 2, 3, 4, 5])
# 2.内積を求める


def dot_product(list1, list2):
    sumProduct = sum([x * y for x, y in zip(list1, list2)])
    print(f"{inner_productA}と{inner_productB}の内積は{sumProduct}です")


inner_productA = [1, 2, 3]
inner_productB = [4, 5, 6]
dot_product(inner_productA, inner_productB)
# 3.回文かどうか判定する
# 4.フィボナッチ数列のn番目を求める(sequence)
# フィボナッチ数列のn番目までの総和を求める
# 指定した値がフィボナッチ数列に含まれるか認識し、含まれる場合は総和を求める
# 値が含まれる場合はそこまでの配列と和を求める
# 5.リスト内で最大値・最小値を求める
