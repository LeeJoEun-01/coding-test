#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 17298                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/17298                          #+#        #+#      #+#     #
#    Solved: 2024/10/02 15:54:54 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))

stack = [0]
result = [-1]*N

for i in range(1, N):
  while stack and arr[stack[-1]] < arr[i]:
    result[stack.pop()] = arr[i]
  stack.append(i)

print(*result)