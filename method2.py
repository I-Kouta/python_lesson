# 指定した文字列が〜以降
pta = 'Perfume'

# 最初に現れる位置をインデックスで返す,該当が無ければ-1
# indexメソッドだと-1ではなくエラー
print(pta.find('e'))  # 1
print(pta.find('g'))  # -1
print('\n')
# 最後に現れるインデックスを取得(rindexも同様)
print(pta.rfind('e'))  # 6
print(pta.rfind('ume'))  # 4
print('\n')
# countメソッド：大文字と小文字の区別アリ
print('Spinning World'.count('n'))  # 3
print('Spinning World'.count('s'))  # 0
print('Spinning World'.count('i', 0, 2))  # Spまでが対象なので0
