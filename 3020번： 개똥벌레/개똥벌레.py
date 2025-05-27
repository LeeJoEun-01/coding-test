#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 3020                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/3020                           #+#        #+#      #+#     #
#    Solved: 2024/09/09 17:51:47 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

N, H = map(int, sys.stdin.readline().split())
cave = [0]*(H)

down = [0]*(H)
up = [0]*(H)

for i in range(N):
  h = int(sys.stdin.readline().rstrip())
  if i%2 != 0: #홀수 -> 석순
    up[h-1] += 1
  elif i%2 == 0: #짝수 -> 종유석
    down[h-1] += 1

print(down)
print(up)
print("======")
down.reverse()
up.reverse()

for i in range(1,H):
  up[i] += up[i-1]
  down[i] += down[i-1]

down.reverse()
for i in range(H):
  cave[i] = down[i] + up[i]

min_value = min(cave)
print(min_value, end=" ")
print(cave.count(min_value))