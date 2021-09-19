# 標準入力を受け付ける。
N = int(input())

ans = []
# Nが0になるまで継続する。
while N > 0:
    # 現在のNの値が奇数の場合、Aの魔法を挟む。
    if not N % 2 == 0:
        ans.append('A')
        N = N - 1
    # Aの魔法を最後にN=0になることを考慮する。
    if N == 0:
        break
    # 偶数のNに対してBの魔法を利用する。
    ans.append('B')
    # // : 小数点以下を切り捨てるため。
    # 参考 : https://www.tohoho-web.com/python/operators.html
    N = N // 2

# 後ろから魔法を利用しているので、反転処理を行う。
# reverse : https://note.nkmk.me/python-reverse-reversed/
ans.reverse()
# join : https://note.nkmk.me/python-split-strip-list-join/
print(''.join(ans))
