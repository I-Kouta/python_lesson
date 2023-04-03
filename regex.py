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

patC = re.compile(r"59nh")
resultPatC = patC.search(target64)
if resultPatC:
    print(resultPatC.group() + "は存在します")
else:
    print("一致しません")
print("\n")


def checkMatch(target64, pattern):
    resultPatD = pattern.search(target64)
    if resultPatD:
        print(resultPatD.group(0))
    else:
        print("マッチしません")


pattern = re.compile(r"jy59")
checkMatch("496, fd3r, 59", pattern)
checkMatch("grape, cherry", pattern)
