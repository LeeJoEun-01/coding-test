import sys
input = sys.stdin.readline

word1 = list(input().rstrip())
word2 = list(input().rstrip())

n1 = len(word1)
n2 = len(word2)

dp = [0]*(n2)

for i in range(n1):
    count = 0
    for j in range(n2):
        if count < dp[j]:
            count = dp[j]
        elif word1[i] == word2[j]:
            dp[j] = count + 1
    # print(dp)
print(max(dp))