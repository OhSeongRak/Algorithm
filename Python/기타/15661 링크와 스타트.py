import sys

input = sys.stdin.readline


def recur(index, start, link, team):  # start는 0번 선수가 있는 팀
    global answer

    answer = min(answer, abs(link - start))

    if index == N:
        return

    if start > link:  # 스타트가 링크보다 더 커지면 의미 없음
        return

    s, l = 0, 0  # index가 스타트 팀에 들어가면서 오르는 능력치 & 줄어드는 능력치
    for i in range(N):
        if i in team:
            s += board[index][i] + board[i][index]
        else:
            l += board[index][i] + board[i][index]

    recur(index + 1, start + s, link - l, team + [index])  # index를 스타트 팀에 넣음
    recur(index + 1, start, link, team)  # index를 팀에 안넣음

    return


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
answer = sys.maxsize
total = 0
for r in range(N):
    total += sum(board[r])

recur(1, 0, total, [0])  # 0번 팀에 1번부터 넣을까? 말까? 시작
print(answer)
