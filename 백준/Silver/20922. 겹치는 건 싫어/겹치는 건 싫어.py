import sys
from collections import defaultdict
input = sys.stdin.readline

N, K = map(int, input().split())
inputs = list(map(int, input().split()))
answer = 0

start = 0
end = 0

count = defaultdict(int)

while end < N:
    if count[inputs[end]] >= K:
        count[inputs[start]] -= 1
        start += 1
    else:
        count[inputs[end]] += 1
        end += 1
        answer = max(answer, end - start)

print(answer)