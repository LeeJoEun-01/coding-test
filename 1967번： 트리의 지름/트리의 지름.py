#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1967                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1967                           #+#        #+#      #+#     #
#    Solved: 2024/09/05 00:18:47 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
sys.setrecursionlimit(10**5)

N = int(sys.stdin.readline().rstrip())
node_info = [list(map(int, sys.stdin.readline().split())) for _ in range(N-1)]
tree = [[] for _ in range(N+1)]

for node in node_info:
  tree[node[0]].append([node[1], node[2]])
  tree[node[1]].append([node[0], node[2]])

visited = [-1]*(N+1)
sum = 0

def dfs(root):
  global sum
  global visited
  global weight

  for node in tree[root]:
    if visited[node[0]] == -1:
      sum += node[1]
      visited[node[0]] = sum
      dfs(node[0])
      sum -= node[1]
  
  return 

visited[1] = 0
dfs(1)
max_weight = max(visited)
max_index = visited.index(max_weight)

sum = 0
visited = [-1]*(N+1)
visited[max_index] = 0
dfs(max_index)

print(max(visited))