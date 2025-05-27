#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1744                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1744                           #+#        #+#      #+#     #
#    Solved: 2025/01/12 23:34:34 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
input = sys.stdin.readline

N =  int(input())
arr = []
for _ in range(N):
  arr.append(int(input().rstrip()))
# 순서대로 접근하기 위해 정렬
arr.sort()

answer = 0
slice_n = -1

if N == 1:
  print(arr[0])
else:
  for i in range(N-1,-1,-2):
    # 만약에 N이 홀수라서 2개씩 계산을 못하면 i 하나만 계산
    if i-1 < 0:
      answer += arr[i]
      continue
    
    # i-1과 i번째 수가 음수라면 slice하고 현재 for문 탈출
    if arr[i-1] < 0 or arr[i] < 0:
      slice_n = i
      break
    
    # 두 수를 곱한 수 저장
    target = arr[i-1]*arr[i]

    if target > 0:
      # 근데 둘 중에 하나가 1이면 곱하는 것보다 더하는 것이 최대임
      if arr[i] == 1 or arr[i-1] == 1:
        answer += 1
      answer += target
    else:
      # 만약 둘 중에 하나가 0이라면
      if target == 0:
        if arr[i] == 0:
          # 곱하는 것이 아니라 더하는 것이 최대
          answer += arr[i]+arr[i-1]
        elif arr[i-1] == 0:
          # 만약에 i-2번째 수가 음수면 0을 곱하면 무효가 되기 때문에 0까지 포함해서 슬라이스
          if i-2 >= 0 and arr[i-2] < 0:
            answer += arr[i]
            slice_n = i-1
            break
          else:
            answer += arr[i]+arr[i-1]
      else:
        answer += arr[i]+arr[i-1]
    # print(f"answer={answer}")
  
  slice_arr = arr[:slice_n+1]  
  # print(f"=== slice_n: {slice_n}")
  # print(f"= arr: {slice_arr}")

  if slice_n >= 0:
    # 음수일때 도는 반복문
    for i in range(0,slice_n+1,2):
      # print(f"======= f{i}")
      if i+1 > slice_n:
        answer += arr[i]
        break
      # 두 수의 곱이 음수면
      if arr[i]*arr[i+1] < 0:
        # 더하는 것이 최대
        answer += arr[i]+arr[i+1]
      else:
        # 양수면 곱하는 것이 최대
        answer += arr[i]*arr[i+1]
  
  print(answer)
