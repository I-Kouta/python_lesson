# 指定した文字列が〜以降
pta = 'Perfume'

# 最初に現れる位置をインデックスで返す,該当が無ければ-1
# indexメソッドだと-1ではなくエラー
print(pta.find('e'))  # 1
print('\n')
# 最後に現れるインデックスを取得(rindexも同様)
print(pta.rfind('e'))  # 6
print(pta.rfind('ume'))  # 4
