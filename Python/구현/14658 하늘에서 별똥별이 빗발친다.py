import sys

input = sys.stdin.readline


def check(r1, c1, r2, c2):
    if r2 <= r1 and c1 <= c2 and r1 - r2 <= L and c2 - c1 <= L:
        return True
    return False


def solution():
    answer = 0

    for r1, c1 in stars:  # 왼쪽 모서리에 있는 별
        for r2, c2 in stars:  # 위쪽 모서리에 있는 별
            if not check(r1, c1, r2, c2):  # 두 별이 왼쪽, 오른쪽 모서리에 위치할 수 있는지 체크
                continue

            r, c = r2, c1
            count = 0
            for x, y in stars:
                if r <= x <= r + L and c <= y <= c + L:
                    count += 1

            answer = max(answer, count)

    return K - answer


N, M, L, K = map(int, input().split())
stars = [list(map(int, input().split())) for _ in range(K)]
print(solution())
