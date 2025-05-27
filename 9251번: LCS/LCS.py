#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9251                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9251                           #+#        #+#      #+#     #
#    Solved: 2025/05/10 16:19:09 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

word1 = list(input().rstrip())
word2 = list(input().rstrip())

n1 = len(word1)
n2 = len(word2)

dp = [[0]*(n1+1) for _ in range(n2+1)]
print(dp)

for i in range(1, n2+1):
    for j in range(1, n1+1):
        if word1[j-1] == word2[i-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])
        # print(dp)
print(max(dp))
