# 次、文字クラスを使って
import re
pat1 = re.compile(r"Sun")
print(bool(pat1.search("Sunset")))  # 日没,true
print(bool(pat1.search("sunglasses")), "\n")  # サングラス,false

pat2 = re.compile(r"s.n")
pat2_0 = re.compile(r"s..n")
print(bool(pat2.search("sunset")))  # .(ドット)が任意の一文字に相当する,true
print(bool(pat2.search("soon")))  # false
print(bool(pat2_0.search("soon")), "\n")  # true

pat3 = re.compile(r"Gl[ny]")
pat3_0 = re.compile(r"Gl[^ny]")
print(bool(pat3.search("Gln")))  # グルタミン,true
print(bool(pat3.search("Glu")))  # グルタミン酸,false
print(bool(pat3.search("Gly")))  # グリシン,true
print(bool(pat3_0.search("Glu")), "\n")  # nとyを含まない場合なのでtrue

pat4 = re.compile(r"\d{3}-\d{4}-\d{4}")  # \d:0-9の意味
print(bool(pat4.search("090-1111-2222")))  # true
print(bool(pat4.search("09011112222")))  # false
print(bool(pat4.search("111-2222")), "\n")  # false

pat5 = re.compile(r"^198")  # 先頭にマッチ,\Aと同様
pat5_0 = re.compile(r"198$")  # 末尾でマッチ,\Zと同様
print(bool(pat5.search("1988-09-20")))  # true
print(bool(pat5.search("1988/09/20")))  # true
print(bool(pat5.search("1996-02-10")))  # false
print(bool(pat5.search("002-2198")))  # false
print(bool(pat5_0.search("002-2198")), "\n")  # true

pat10 = re.compile(r"be{2}n")  # *:0回以上、?:0回か1回
pat10_0 = re.compile(r"be{1,4}n")  # 1, 4みたいにスペースは不可
print(bool(pat10.search("been")))  # true
print(bool(pat10.search("ben")))  # false
print(bool(pat10_0.search("ben")))  # true
print(bool(pat10_0.search("beeeeen")), "\n")  # false

pat11 = re.compile(r"<em>.*</em>")
msg11 = "<p>今日は<em>快晴の</em>一日です</p>"
result11 = pat11.search(msg11)
print(result11.group(0), "\n")

pat12 = re.compile(r"[0-9]{3}-[0-9]{4}")
msg12 = "郵便番号:111-2222"
result12 = pat12.search(msg12)
print(result12.group(0), "\n")

# 数字が1-3つのあと.が続く+1-3つの数値,\.は.を文字として認識させるため
pat13 = re.compile(r"(\d{1,3}\.){3}\d{1,3}")
msg13 = "IPアドレスは123.432.0.232です"
result13 = pat13.search(msg13)
print(result13.group(0), "\n")

pat14 = re.compile(r"\d{3}-\d{4}-\d{4}|\d{11}")
print(bool(pat14.search("080-0226-0334")))  # true
print(bool(pat14.search("08002260334")))  # true
print(bool(pat14.search("0120-111-222")))  # false
print(bool(pat14.search("000-1111")))  # false
