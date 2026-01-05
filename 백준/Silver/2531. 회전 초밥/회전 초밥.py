import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
arr = [int(input().rstrip()) for _ in range(N)]
answer = 0

for i in range(N):
    if i+k-1 <= N:
        tmp = arr[i:i+k]
    else:
        tmp = arr[i:]+arr[:(k-(N-i))]

    len_max = len(set(tmp))
    if c not in tmp:
        answer = max(answer, len_max+1)
    else:
        answer = max(answer, len_max)

print(answer)