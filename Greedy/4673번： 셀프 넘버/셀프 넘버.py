#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 4673                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/4673                           #+#        #+#      #+#     #
#    Solved: 2024/07/22 16:51:21 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

arr = [False for i in range(10001)]

for i in range(1,9990):
  if i > 0 and i < 10:
    index = i + i
  elif i >= 10 and i < 100:
    index = i + i//10 + i%10
  elif i >= 100 and i < 1000:
    index = i + i//100 + (i//10)%10 + i%10
  elif i >= 1000 and i < 10000:
    index = i + i//1000 + (i//100)%10 + (i//10)%10 + i%10
  
  if index <= 10000:
    arr[index] = True

for i in range(1,10001):
  if arr[i] == False:
    print(i)