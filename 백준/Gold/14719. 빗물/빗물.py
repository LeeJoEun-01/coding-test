import sys
input = sys.stdin.readline

H, W = map(int, input().split())
height = list(map(int, input().split()))
answer = 0

for i in range(1, W-1):
    left_max = max(height[:i])
    right_max = max(height[i+1:])
    h = min(left_max, right_max)
    if h > height[i]:
        answer += (h-height[i])

print(answer)