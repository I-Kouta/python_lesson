# パターンとマッチする
import re


def checkMatch(msg, pat):
    pattern = re.compile(pat)
    result = pattern.fullmatch(msg)
    if result:
        print(result.group(0))
    else:
        print("完全一致しません")


checkMatch("シークレットシークレット", r"シ.*シ")  # 一致しません
checkMatch("シークレットシークレット", r"シ.*ト")  # シークレットシークレット
