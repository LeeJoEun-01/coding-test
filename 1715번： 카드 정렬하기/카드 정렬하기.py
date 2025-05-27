#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1715                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1715                           #+#        #+#      #+#     #
#    Solved: 2024/08/06 00:50:39 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from queue import PriorityQueue

N = int(sys.stdin.readline())
priority_queue = PriorityQueue()
for _ in range (N):
  card = int(sys.stdin.readline())
  priority_queue.put(card)

answer = 0 # 답
sum = 0# 단계마다의 합

if N != 1:
  while(True):
    min1 = priority_queue.get()
    min2 = priority_queue.get()
    sum = min1+min2
    priority_queue.put(sum)
    answer += sum
    if priority_queue.qsize() == 0:
      break
    elif priority_queue.qsize() == 1:
      break

print(answer)