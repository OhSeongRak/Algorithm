def check():
    print(selected)
    return


def recur(cur, count):
    if count == 0:
        return

    if cur == m - 1:
        selected[cur] = count
        check()
        return

    for i in range(1, count + 1):
        selected[cur] = i
        recur(cur + 1, count - i)

    return


total, m = 20, 10
selected = [0] * 10
recur(0, total)
