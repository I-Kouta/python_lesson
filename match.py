# マッチオブジェクトからマッチした文字列の情報を取得
import re
msg1 = 'birthday is 1989/02/15'
pat1 = re.compile(r"(\d{4})/(\d{2})/(\d{2})")
result1 = pat1.search(msg1)
if result1:
    print("生年月日：" + result1.group(0))
    print("年：" + result1.group(1))
    print("月：" + result1.group(2))
    print("日：" + result1.group(3))

print("\n")
msg2 = 'birthday is 1999/02/03'
pat2 = re.compile(r"(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})")
result2 = pat2.search(msg2)
if result2:
    print("マッチ：" + result2.group(0))
    print("group[年]：" + result2.group("year"))
    print("group[月]：" + result2.group("month"))
    print("group[日]：" + result2.group("day"))
