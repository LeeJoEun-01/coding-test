#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9935                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9935                           #+#        #+#      #+#     #
#    Solved: 2024/10/01 19:19:49 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

arr = list(str(sys.stdin.readline().rstrip()))
eStr = list(str(sys.stdin.readline().rstrip()))
num = len(eStr)

stack = []

for char in arr:
  stack.append(char)
  if stack[len(stack)-num:len(stack)+1] == eStr:
    for _ in range(num):
      stack.pop()

if len(stack) == 0:
  print("FRULA")
else:
  print("".join(stack))