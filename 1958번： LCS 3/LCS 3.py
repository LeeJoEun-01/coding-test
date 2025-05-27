#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1958                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1958                           #+#        #+#      #+#     #
#    Solved: 2024/11/19 12:39:24 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

arr = []
for _  in range(3):
  input = str(sys.stdin.readline().rstrip())
  arr.append([input, len(input)])

arr.sort(key = lambda x: x[1])

target = arr[0][0]
result = []
answer = 0

for i in range(1,3):
  word = ""
  j = 0

  while j < len(target)-1:
    for ch in arr[i][0]:
      if j > len(target)-1:
        break
      #print(f"=== char: {target[j]} | ch: {ch}")
      if target[j] == ch:
        word += ch
        j += 1
    j += 1
  result.append([word, len(word)])

result.sort(key = lambda x: x[1], reverse=True)

print(result[0][1])
