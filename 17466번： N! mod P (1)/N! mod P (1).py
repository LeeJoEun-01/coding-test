#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 17466                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/17466                          #+#        #+#      #+#     #
#    Solved: 2025/01/20 14:29:32 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

N, P = map(int, sys.stdin.readline().split())
answer = 1

for i in range(2,N+1):
  answer = (answer*i)%P

print(answer%P)