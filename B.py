# 標準入力を受け付ける。
N = int(input())

A = []
for _ in range(N):
    # スペース区切りで姓名が入力されるが、分離して考えず姓 名をひと組として考える。
    A.append(str(input()))

# 姓 名の重複削除を行う。
# set : https://note.nkmk.me/python-set/
A = set(A)

# Nと姓 名の数が同数でない場合、同姓同名は存在する。
if N != len(A):
    print('Yes')
# Nと姓 名の数が同数の場合、同姓同名は存在しない。
else:
    print('No')
