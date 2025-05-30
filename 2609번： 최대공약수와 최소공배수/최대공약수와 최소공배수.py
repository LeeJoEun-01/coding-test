#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2609                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2609                           #+#        #+#      #+#     #
#    Solved: 2025/01/20 15:26:57 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
import math

A, B = map(int, sys.stdin.readline().split())

print(math.gcd(A,B))
print(math.lcm(A,B))
