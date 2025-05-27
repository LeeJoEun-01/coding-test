# Sort
# 1141. 접두사

import sys

n = int(sys.stdin.readline().strip())

words = [sys.stdin.readline().strip() for _ in range(n)]
words.sort(key=len)

# print(words)

for i in range(n):
    length = len(words[i])
    # print("========")
    for j in range(i+1, n):
        word = words[j]
        target = word[0:length]
        # print(word)
        # print(target)
        # print()
        if words[i] == target:
            words[i] = 0

print(n-words.count(0))
