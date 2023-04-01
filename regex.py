# 正規表現
import re
target64 = "495j6t9h4jy59nhjt049ehd8gbhetognbodoj988t7tgubuvcrtdr0j9ihbyvcty"
# print(len(target64))
pattern = re.compile(r'n...o')  # n---oがあれば返す
result = pattern.search(target64)
if result:
    print(result.group())
