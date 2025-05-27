#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1863                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1863                           #+#        #+#      #+#     #
#    Solved: 2025/04/05 16:36:16 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

N = int(input().strip())

skyline = []
for _ in range(N):
  x, y = map(int, input().split())
  skyline.append(y)
skyline.append(0)

cnt = 0
arr = [0]
for h in skyline:
  height = h
  while arr[-1] > h:
    print(f"= arr: {arr}  | top: {arr[-1]} | height: {height}")
    if arr[-1] != height:
      cnt += 1
      height = arr[-1]
      print(f"= count: {cnt} | height: {height}")
    arr.pop()
  arr.append(h)

print(cnt)