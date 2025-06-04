import sys
input = sys.stdin.readline


def check(arr, n):
    i = 0
    while i < n-1:
        nn = len(arr[i])
        tmp = arr[i+1][:nn]
        if arr[i] == tmp:
            return print("NO")
        i += 1
    return print("YES")


N = int(input().rstrip())
for _ in range(N):
    n = int(input().rstrip())
    inputs = [list(input().rstrip()) for _ in range(n)]

    inputs.sort()
    # print(f"== inputs: {inputs}")
    check(inputs, n)