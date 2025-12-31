import sys
input = sys.stdin.readline

N, D = map(int, input().split())
inputs = []
for i in range(N):
    x, y, w = map(int, input().split())
    inputs.append([x, y, w])
inputs.sort(key=lambda x: (x[1], x[0]))

dp = [0]*(D+1)
idx = 0
for i in range(1, D+1):
    dp[i] = dp[i-1]+1

    while idx < N:
        if inputs[idx][1] == i:
            if inputs[idx][1] <= D:
                x, y, w = inputs[idx]
                dp[i] = min(dp[i], dp[x]+w)
            idx += 1
        else:
            break

# print(dp)
# print()
print(dp[D])