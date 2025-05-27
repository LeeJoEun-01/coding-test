#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2533                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2533                           #+#        #+#      #+#     #
#    Solved: 2025/02/04 02:38:16 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = []
graph = [[] for _ in range(N+1)]
d = 0
before_a = 0

for _ in range(N-1):
  a, b = map(int, input().split())
  if before_a != a:
    d += 1
    before_a = a
  graph[a].append(b)

depth = 0
d_arr = graph[1]
dp = [0]*(N+1)

while depth <= d:
  depth += 1
  new_arr = []
  for i in d_arr:
    if len(graph[i]) != 0:
      new_arr += graph[i]
  d_arr = new_arr
  dp[depth] = dp[depth-1]+len(d_arr)

print(dp)
print(dp[d])
