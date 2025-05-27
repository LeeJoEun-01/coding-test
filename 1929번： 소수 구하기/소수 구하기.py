#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1929                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1929                           #+#        #+#      #+#     #
#    Solved: 2025/01/20 15:57:51 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

isErased = [0]*1000001
M, N = map(int, sys.stdin.readline().split())

isErased[1] = 1

i = 2
while i*i <= 1000000:
  if isErased[i] == 0:
    for j in range(i*i, 1000001, i):
      isErased[j] = 1
  i += 1

for j in range(M, N+1):
  if isErased[j] == 0:
    print(j)
