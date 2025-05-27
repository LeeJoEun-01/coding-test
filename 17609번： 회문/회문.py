#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 17609                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/17609                          #+#        #+#      #+#     #
#    Solved: 2024/11/26 00:47:57 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

T = int(sys.stdin.readline().rstrip())
arr = []

for _ in range(T):
  input = list(sys.stdin.readline().rstrip())
  arr.append(input)

for i in range(T):
  target = arr[i]
  n = len(target)
  result = 0

  start = 0
  end = n-1

  while start < end:
    if target[start] != target[end]:
      if target[start+1] == target[end]:
        temp = target[:start] + target[start+1:]
        if temp[:] == temp[::-1]:
          result = 1
          break
      if target[start] == target[end-1]:
        temp = target[:end] + target[end+1:]
        if temp[:] == temp[::-1]:
          result = 1
          break
      
      result = 2
      break

    else:
      start += 1
      end -= 1

  print(result)

