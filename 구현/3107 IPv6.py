import sys

input = sys.stdin.readline


def solution():
    lst = reduce.split(":")
    zero = lst.count('')
    for i in range(zero - 1):
        lst.remove('')

    answer = ''
    for k in lst:
        if k == '':
            zero_group = 8 - (len(lst) - 1)
            for _ in range(zero_group):
                answer += "0000:"
        else:
            answer += '0' * (4 - len(k)) + k
            answer += ":"

    return answer[:-1]


reduce = input().rstrip()
print(solution())
