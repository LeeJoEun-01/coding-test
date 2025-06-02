import sys

word = list(sys.stdin.readline().rstrip())
result = [-1]*26
for i in range(len(word)):
    w = word[i]
    index = ord(w)
    if result[index-97] == -1:
        result[index-97] = i
print(*result)