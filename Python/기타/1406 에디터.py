import sys

input = sys.stdin.readline


def solution():
    for oper in editor:
        if oper == 'L' and left:
            right.append(left.pop())
        elif oper == 'D' and right:
            left.append(right.pop())
        elif oper == 'B' and left:
            left.pop()
        elif oper not in ['L', 'D', 'B']:
            left.append(oper)

    for k in right[::-1]:
        left.append(k)

    return "".join(left)


if __name__ == "__main__":
    left = list(input().strip())
    right = []
    N = int(input())
    editor = []
    for _ in range(N):
        tmp = list(input().split())
        if tmp[0] == 'P':
            editor.append(tmp[1])
        else:
            editor.append(tmp[0])

    print(solution())
