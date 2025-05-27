#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1717                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1717                           #+#        #+#      #+#     #
#    Solved: 2024/10/26 01:36:58 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
sys.setrecursionlimit(1000**2)

N, M = map(int, sys.stdin.readline().split())
parent = [i for i in range(N+1)]

def find_parent(x):
  if parent[x] != x:
    parent[x] = find_parent(parent[x])
  return parent[x]

def union_parent(first, second):
  parent1 = find_parent(first)
  parent2 = find_parent(second)

  if parent1 < parent2:
    parent[parent2] = parent1
  else:
    parent[parent1] = parent2

for i in range(M):
  num, first, second = map(int, sys.stdin.readline().split())

  if num == 0:
    #합집합
    union_parent(first, second)
  else:
    # 확인 연산
    if find_parent(first) == find_parent(second):
       print("YES")
    else:
       print("NO")
  