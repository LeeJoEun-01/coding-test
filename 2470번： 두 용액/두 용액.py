#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2470                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2470                           #+#        #+#      #+#     #
#    Solved: 2024/09/11 18:09:43 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

start = 0
end = N-1

answer = abs(arr[start]+arr[end])
result = [arr[start],arr[end]]

while start < end:
  sum = arr[start]+arr[end]
  if  abs(sum) < answer:
    answer = abs(sum)
    result = [arr[start],arr[end]]

  if sum > 0:
    end -= 1
  elif sum < 0:
    start += 1
  else:
    break
  
print(result[0], result[1])