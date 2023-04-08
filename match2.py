# 次、文字クラスを使って
import re
pat1 = re.compile(r"Sun")
print(bool(pat1.search("Sunset")))  # 日没,true
print(bool(pat1.search("sunglasses")), "\n")  # サングラス,false

pat2 = re.compile(r"s.n")
pat2_0 = re.compile(r"s..n")
print(bool(pat2.search("sunset")))  # .(ドット)が任意の一文字に相当する,true
print(bool(pat2.search("soon")))  # false
print(bool(pat2_0.search("soon")))  # true
