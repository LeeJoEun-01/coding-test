#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 23971                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/23971                          #+#        #+#      #+#     #
#    Solved: 2025/03/28 23:17:35 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
import math
input = sys.stdin.readline

H, W, N, M = map(int, input().split())

col = math.ceil(H/(N+1))
row = math.ceil(W/(M+1))

print(col*row)