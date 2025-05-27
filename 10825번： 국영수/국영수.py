#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10825                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10825                          #+#        #+#      #+#     #
#    Solved: 2025/01/13 14:33:37 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
input = sys.stdin.readline

N = int(input())
arr = [list(input().split()) for _ in range(N)]

arr.sort(key = lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in arr:
  print(student[0])