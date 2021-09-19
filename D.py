# 標準入力を受け付ける。
N, M = map(int, input().split())

# onTopList[x] : 各筒の一番上にあるボールの色(番号)に対応する、筒のindex番号を格納する。
onTopList = [[] for _ in range(N + 1)]

# 筒の中に配置されるボールの色一覧
A = []
# 取り除くことができるボール一覧を格納する。
stack = []

for i in range(M):
    k = int(input())

    # [::-1] : 逆順にしているのは、pop関数を引数指定することなく、利用するため。
    # del関数を利用して、筒の一番上のボールを取り除いているとTLEになってしまう。
    # pop関数, del関数 : https://note.nkmk.me/python-list-clear-pop-remove-del/
    A.append(list(map(int, input().split()))[::-1])

    # 筒の一番上のボールの色を取得する。
    color = A[i][-1]
    # 筒の一番上のボールの色に対応する、筒のindex番号を格納する。
    onTopList[color].append(i)

    # 筒の一番上に同じ色のボールが2つ存在する場合、取り除くことができるのでstackへ格納する。
    if len(onTopList[color]) == 2:
        stack.append(color)

# 取り除いたボールの数を格納する。
doneCnt = 0
# 取り除くことが可能なボールが存在する限りループを回す。
while len(stack) != 0:
    # 取り除くことが可能なボールの色を取得する。
    # 複数stackが溜まっている場合でも順序に問題はない。
    color = stack.pop()

    # ボールを取り除いた数をカウントする。
    doneCnt += 1

    # ボールの色(番号)情報に紐づく、筒のindex番号を取得する。
    x, y = onTopList[color]

    # 筒の一番上に配置されるボールを取り除く。
    # ここでdel関数を利用すると、TLEになる。
    A[x].pop()

    # 筒の中にボールが残っている場合、筒の一番上にあるボールの色(番号)に対応する、筒のindex番号を格納する。
    if len(A[x]) != 0:
        newColor = A[x][-1]
        onTopList[newColor].append(x)
        if len(onTopList[newColor]) == 2:
            stack.append(newColor)

    # 筒の一番上に配置されるボールを取り除く。
    # ここでdel関数を利用すると、TLEになる。
    A[y].pop()

    # 筒の中にボールが残っている場合、筒の一番上にあるボールの色(番号)に対応する、筒のindex番号を格納する。
    if len(A[y]) != 0:
        newColor = A[y][-1]
        onTopList[newColor].append(y)
        if len(onTopList[newColor]) == 2:
            stack.append(newColor)

# 取り除いたボールの数が、Nに等しければYes、そうでなければNoを返す。
if doneCnt == N:
    print("Yes")
else:
    print("No")
