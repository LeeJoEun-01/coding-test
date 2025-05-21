import sys
from collections import deque

inputs = list(sys.stdin.readline())
arr = []
stack = deque([])

for c in inputs:
    if c == "(":
        arr.append(-1)
    elif c == ")":
        arr.append(-4)
    elif c == "[":
        arr.append(-2)
    elif c == "]":
        arr.append(-3)

i = 0
while i < len(arr):
    if len(stack) != 0:
        prev = stack.pop()
        if prev < 0:
            n = prev+arr[i]
            if prev+arr[i] == -5:  # 괄호 맞다!
                if prev == -1:
                    stack.append(2)
                else:
                    stack.append(3)
            else:
                stack.append(prev)
                stack.append(arr[i])
        else:  # 괄호가 아니라 숫자인 경우
            if len(stack) != 0:
                pprev = stack.pop()
                if pprev < 0:
                    if pprev+arr[i] == -5:  # 괄호 맞다!
                        if arr[i] == -4:
                            stack.append(prev*2)
                        elif arr[i] == -3:
                            stack.append(prev*3)
                    else:
                        stack.append(pprev)
                        stack.append(prev)
                        stack.append(arr[i])
                else:
                    stack.append(pprev+prev)
                    i -= 1
            else:
                stack.append(prev)
                stack.append(arr[i])
    else:
        stack.append(arr[i])
    i += 1

    # print(f"== i: {i} | stack: {stack}")

ans = 0
for s in stack:
    if s < 0:
        ans = 0
        break
    else:
        ans += s
print(ans)