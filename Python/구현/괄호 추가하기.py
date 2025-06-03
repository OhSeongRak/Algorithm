import sys

input = sys.stdin.readline


def cal(n1, o, n2):
    if o == '+':
        return n1 + n2
    if o == '-':
        return n1 - n2
    if o == '*':
        return n1 * n2


def solution(N, lst):
    numbers = [int(i) for i in lst if i.isdigit()]
    opers = [i for i in lst if not i.isdigit()]
    selected = [False] * (N // 2)
    answer = -sys.maxsize


    def recur(index):
        nonlocal numbers, opers, selected, answer

        if index == (N // 2):
            num_stack, oper_stack = [], []
            num_stack.append(numbers[0])
            for i in range(len(selected)):
                if selected[i]:
                    num_stack.append(cal(num_stack.pop(), opers[i], numbers[i + 1]))
                else:
                    num_stack.append(numbers[i + 1])
                    oper_stack.append(opers[i])

            tmp = num_stack[0]
            for i in range(len(oper_stack)):
                tmp = cal(tmp, oper_stack[i], num_stack[i+1])

            answer = max(answer, tmp)
            return

        if not selected[index - 1]:
            selected[index] = True
            recur(index + 1)

        selected[index] = False
        recur(index + 1)

        return

    recur(0)

    return answer


N = int(input())
lst = list(input().strip())
print(solution(N, lst))
