import sys
input = sys.stdin.readline

H, W = map(int, input().split())
block = list(map(int, input().split()))
ans = 0

for i in range(1, W-1):
    current = block[i]
    left_max = max(block[:i+1])
    right_max = max(block[i+1:])
    min_h = min(left_max, right_max)

    tmp = min_h-current
    if tmp >= 0:
        ans += tmp

print(ans)