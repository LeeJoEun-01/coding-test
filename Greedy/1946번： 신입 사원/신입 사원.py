#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1946                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1946                           #+#        #+#      #+#     #
#    Solved: 2024/08/02 17:49:47 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

def recruit(N, arr):
  count = N #인원수
    
  target = arr[0]
  for i in range(1,N):
    if target[1] < arr[i][1]:
        count -= 1
    else:
      target = arr[i]

  return count


T = int(input()) # 테스트케이스

for i in range(T):
  arr = []
  N = int(input()) # 인원수
  for j in range(N):
    arr.append(list(map(int, input().split())))
  sortedArr = sorted(arr, key=lambda x: x[0])
  result = recruit(N, sortedArr)
  print(result)
