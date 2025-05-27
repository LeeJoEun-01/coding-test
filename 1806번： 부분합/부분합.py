#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1806                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1806                           #+#        #+#      #+#     #
#    Solved: 2024/09/10 17:48:47 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

start = 0 # 인덱스 위치
end = N-1

# 부분합 만들어두기
sum = 0
sum_arr = [0]
for i in arr:
  sum += i
  sum_arr.append(sum)

target = sum_arr[end+1]-sum_arr[start]
while start <= end:
  if target >= S:
    start += 1
    print(f"=== start: {start} | target: {target}")
  else:
    break
  target = sum_arr[end+1]-sum_arr[start]

print(f"=== start: {start} | end: {end}")

last_value = sum_arr.pop()

if S > last_value:
  print(0)
else:
  print(end+1-(start-1))