#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 12851                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/12851                          #+#        #+#      #+#     #
#    Solved: 2024/08/18 12:28:59 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

queue = deque()

def bfs(N, K):
  value = N
  count = 0
  queue.append([value, count])
  under = 100000

  while(count < under):
    value, count = queue.popleft()
    newValue = [0, 0, 0]
    newCount = 0

    for i in range(3):
      newCount  = count + 1
      if i == 0:
        newValue[0] = value - 1
        queue.append([newValue[0], newCount])

      elif i == 1:
        if value >= K:
          break
        newValue[1] = value + 1
        if newValue[1] != newValue[0]:
          queue.append([newValue[1], newCount])

      elif i == 2:
        if value >= K:
          break
        newValue[2] = value*2
        if newValue[2] != newValue[0] or newValue[2] != newValue[1]:
          queue.append([newValue[2], newCount])

    if K in newValue:
      under = newCount

  # print(queue)
  return newCount-1

count = bfs(N, K)
# print(queue)

result = 0
for i in queue:
  if i[0] == K and i[1] == count:
    result += 1

print(count)
print(result)