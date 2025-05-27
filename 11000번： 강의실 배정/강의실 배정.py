#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11000                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11000                          #+#        #+#      #+#     #
#    Solved: 2024/12/05 17:02:23 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
import heapq

N = int(sys.stdin.readline().rstrip())
arr = []

for _ in range(N):
  a, b = map(int, sys.stdin.readline().split())
  arr.append([a,b])

arr.sort(key = lambda x: x[0])
heap = []

heapq.heappush(heap, arr[0][1])

for i in range(1,len(arr)):
  if arr[i][0] >= heap[0]:
    heapq.heappop(heap)
  heapq.heappush(heap, arr[i][1])

print(len(heap))
