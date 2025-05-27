#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2161                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2161                           #+#        #+#      #+#     #
#    Solved: 2025/01/09 19:31:26 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
import queue

N = int(sys.stdin.readline().rstrip())

arr = [ i+1 for i in range(N)]
data = queue.Queue(arr)
result = []

while True:
  if data.qsize() <= 1:
    break

  val1 = data.get()
  result.append(val1)
  val2 = data.get()
  data.put(val2)

print(*result)