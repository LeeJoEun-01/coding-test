#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 15654                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/15654                          #+#        #+#      #+#     #
#    Solved: 2024/08/26 02:08:17 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# import sys
# from itertools import *

# N, M = map(int, sys.stdin.readline().split())
# arr = list(map(int, sys.stdin.readline().split()))
# arr.sort()

# result = list(permutations(arr, M))

# for row in result:
#   for ele in row:
#     print(ele, end=" ")
#   print()


import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort()
visited = [False]*(N+1)
result = []

def dfs():
  if len(result) == M:
    print(' '.join(map(str, result)))
    return

  for i in range(1, N+1):
    if not visited[i]:
      visited[i] = True
      result.append(arr[i-1])
      dfs()
      result.pop()
      visited[i] = False

dfs()