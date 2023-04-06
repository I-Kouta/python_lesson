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
