#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2776                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2776                           #+#        #+#      #+#     #
#    Solved: 2025/01/28 02:03:32 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
input = sys.stdin.readline

def binary_search(target, arrN):
  start = 0
  end = len(arrN)-1

  while start <= end:
    mid = (start+end)//2

    if target < arrN[mid]:
      end = mid-1
    elif target > arrN[mid]:
      start = mid+1
    else:
      return 1
  return 0


T = int(input().rstrip())

for t in range(T):
  N = int(input().rstrip())
  arrN = list(map(int, input().split()))
  M = int(input().rstrip())
  arrM = list(map(int, input().split()))
  
  arrN.sort()

  for i in arrM:
    print(binary_search(i, arrN))
        
