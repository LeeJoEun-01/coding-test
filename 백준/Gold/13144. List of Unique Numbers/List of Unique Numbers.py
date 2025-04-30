import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input().rstrip())
inputs = list(map(int, input().split()))

answer = 0
start = 0
end = 0
tmp = []
dic = defaultdict(int)

while end < N:
    if dic[inputs[end]] == 0:
        dic[inputs[end]] += 1
        # print(f"end: {end} | start: {start}")
        answer += end-start+1
        end += 1
    else:
        dic[inputs[start]] -= 1
        start += 1

print(answer)