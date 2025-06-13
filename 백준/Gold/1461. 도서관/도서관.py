import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
pos = []
neg = []
dist = []

for i in arr:
    if i > 0:
        pos.append(i)
    else:
        neg.append(abs(i))
pos.sort(reverse=True)
neg.sort(reverse=True)

for i in range(len(pos)):
    if i % M == 0:
        dist.append(pos[i])

for i in range(len(neg)):
    if i % M == 0:
        dist.append(neg[i])

dist.sort()
ans = 2*sum(dist)-dist[-1]
print(ans)
