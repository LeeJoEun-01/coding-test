#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1697                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1697                           #+#        #+#      #+#     #
#    Solved: 2025/03/31 15:32:11 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
from collections import deque

MAX = 10**5
cnt = [0]*(MAX+1)
N, K = map(int, sys.stdin.readline().split())

def bfs():
  q = deque()
  q.append(N)

  while q:
    x = q.popleft()

    if x == K:
      print(cnt[x])
      break
      
    for nx in (x-1, x+1, x*2):
      if 0 <= nx <= MAX and not cnt[nx]:
        cnt[nx] = cnt[x]+1
        q.append(nx)

bfs()