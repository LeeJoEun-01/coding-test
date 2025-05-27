#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2312                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2312                           #+#        #+#      #+#     #
#    Solved: 2025/01/20 14:41:07 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
  N = int(sys.stdin.readline().rstrip())
  i = 2
  temp = N
  count = 0
  while i <= N:
    count = 0
    # print(f"temp:{temp} i:{i}")
    while temp%i == 0:
      count += 1
      temp = temp//i
    if count > 0:
      print(i, count)
    i += 1





