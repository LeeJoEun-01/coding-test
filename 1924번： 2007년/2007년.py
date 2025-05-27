#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1924                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1924                           #+#        #+#      #+#     #
#    Solved: 2025/02/19 23:00:41 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
input = sys.stdin.readline

x, y = map(int, input().split())
# 1 28일 이상이면
ans = 0

if x == 2:
  ans = (y+3)%7
elif x == 1:
    ans = y%7
elif x == 4 or x == 6 or x == 9 or x == 11: #짝수
  if x >= 9:
    ans = (y+((x//2+1)*3+(x//2-2)*2))%7
  else:
    ans = (y+((x//2)*3+(x//2-2)*2))%7
else:
  if x >= 9:
    ans = (y+((x//2)*3+(x//2-2)*2))%7
  else:
    if x == 8:
      ans = (y+((x//2)*3+(x//2-2)*2))%7
    else:
      ans = (y+((x//2)*3+(x//2-1)*2))%7

if ans == 1:
  print("MON")
elif ans == 2:
  print("TUE")
elif ans == 3:
  print("WED")
elif ans == 4:
  print("THU")
elif ans == 5:
  print("FRI")
elif ans == 6:
  print("SAT")
elif ans == 0:
  print("SUN")