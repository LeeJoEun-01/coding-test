import sys

input = sys.stdin.readline

N, M = map(int, input().split())
words = [input().rstrip() for _ in range(N)]

max_count = 0
words_dic = {}
for w in words:
    if w not in words_dic:
        words_dic[w] = 1
    else:
        words_dic[w] += 1

note = [0] * 100000
for k, v in words_dic.items():
    if note[v] == 0:
        note[v] = [k]
    else:
        note[v].append(k)

for i in range(99999, 0, -1):
    if note[i] != 0:
        if len(note[i]) == 1:
            if len(note[i][0]) >= M:
                print(note[i][0])
        else:
            target = note[i]
            target.sort(key=lambda x: (-len(x), x))
            for t in target:
                if len(t) >= M:
                    print(t)