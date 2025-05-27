#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14002                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14002                          #+#        #+#      #+#     #
#    Solved: 2025/05/18 12:49:30 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = list(map(int, input().split()))

dp = [[arr[i]] for i in range(N)]

for i in range(N):
    for j in range(i):

        if arr[i] > arr[j]:
            if len(dp[i]) < len(dp[j])+1:
                dp[i] = dp[j] + [arr[i]]

max_length = 0
max_index = 0
for i in range(N):
    if max_length < len(dp[i]):
        max_length = len(dp[i])
        max_index = i

print(len(dp[max_index]))
print(*dp[max_index])
