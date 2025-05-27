#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14267                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14267                          #+#        #+#      #+#     #
#    Solved: 2024/09/19 12:13:56 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
sys.setrecursionlimit(2*10**5)

N , M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

tree = [[] for _ in range(N+1)]

for i in range(N):
  if num[i] != -1:
    tree[num[i]].append(i+1)

result = [0 for _ in range(N)]

def dfs(index, count):
  result[index-1] += count
  if tree[index] != []:
    dfs(i, count)

for i in range(M):
  index = arr[i][0]
  count = arr[i][1]
  dfs(index, count)

print(*result)