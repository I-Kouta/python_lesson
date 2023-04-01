# 正規表現
import re
target64 = "495j6t9h4jy59nhjt049ehd8gbhetognbodoj988t7tgubuvcrtdr0j9ihbyvcta"
# print(len(target64))
pattern = re.compile(r'n...o')  # n---oがあれば返す
result = pattern.search(target64)
if result:
    print(result.group())


pat = re.compile(r"vcta$")  # この文字列で終わっているか
resultPat = pat.search(target64)
if resultPat:
    print("「" + resultPat.group() + "」" + "は末尾でパターンにマッチします")
else:
    print("パターンにマッチしません")
# 別パターン
patB = re.compile(r"$496")  # この文字列で終わっているか
resultPatB = patB.search(target64)
if resultPatB:
    print("「" + resultPatB.group() + "」" + "は先頭でパターンにマッチします")
else:
    print("パターンにマッチしません")
