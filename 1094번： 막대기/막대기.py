#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1094                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1094                           #+#        #+#      #+#     #
#    Solved: 2025/02/16 14:43:00 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
input = sys.stdin.readline

N = int(input().rstrip())
count = 0

while N > 0:
  if N & 1:
    count += 1
  N >>= 1

print(count)

# tmp = 1
# arr = [0]*(N+1)

# while tmp <= N:
#   for i in range(1,tmp):
#     if arr[i] != 0 and i+tmp <= N:
#       arr[i+tmp] = arr[i]+1
#   arr[tmp] = 1
#   tmp *= 2

# print(arr[N])