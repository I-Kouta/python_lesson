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
print(bool(pat4.search("111-2222")))  # false
