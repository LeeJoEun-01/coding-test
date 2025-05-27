#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2744                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2744                           #+#        #+#      #+#     #
#    Solved: 2025/01/09 19:57:51 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

eng = list(sys.stdin.readline().rstrip())
result = []

for ch in eng:
  if ch.isupper():
    result.append(ch.lower())
  else:
    result.append(ch.upper())

print(*result, sep="")