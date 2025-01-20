import sys

input = sys.stdin.readline


def solution():
    return


if __name__ == "__main__":
    N = int(input())
    lst = list(map(int, input().split()))
    print(*lst, sep='\n')
    print(solution())
