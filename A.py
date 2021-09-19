# 標準入力を受け付ける。
# 与えられる数値を文字列として捉える。
S = str(input())

# .区切りでX.Yの値の分離を行う。
# front = X
# back = Y
front, back = S.split('.')

# 型変換を行う。
back = int(back)

# Yの値のif分岐を行う。
if back >= 0 and back <= 2:
    repStr = '-'
elif back >= 3 and back <= 6:
    repStr = ''
else:
    repStr = '+'

# Xの値とYの条件に当てはまる文字(-, '', +)を連結する。
print(front + repStr)
