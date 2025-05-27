#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 13549                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/13549                          #+#        #+#      #+#     #
#    Solved: 2024/10/16 22:43:15 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
import math
import heapq

subin, sister = map(int, sys.stdin.readline().split())
answer = 0
queue = []
heapq.heappush(queue, (0,subin))
visited = [math.inf]*100001
visited[subin] = 0

while queue:
  count, location = heapq.heappop(queue)

  if sister == location:
      answer = count
      break

  if visited[location] < count:
    continue
  for x, y in [(count, location*2), (count+1, location-1), (count+1, location+1)]:
    if 0<= y <= 100000 and visited[y] > x:
      visited[y] = x
      heapq.heappush(queue, (x, y))
  
  # print(queue)

print(answer)