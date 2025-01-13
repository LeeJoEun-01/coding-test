import sys
input = sys.stdin.readline

N =  int(input())
arr = []
for _ in range(N):
  arr.append(int(input().rstrip()))
arr.sort()

answer = 0
slice_n = -1

if N == 1:
  print(arr[0])
else:
  # 더하기
  for i in range(N-1,-1,-2):
    if i-1 < 0:
      answer += arr[i]
      continue

    if arr[i-1] < 0 or arr[i] < 0:
      slice_n = i
      break
    target = arr[i-1]*arr[i]
    # print(f"== target:{target} = {arr[i]}*{arr[i-1]}  | {i}")

    if target > 0:
      if arr[i] == 1 or arr[i-1] == 1:
        answer += 1
      answer += target
    else:
      if target == 0:
        if arr[i] == 0:
          answer += arr[i]+arr[i-1]
        elif arr[i-1] == 0:
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
    for i in range(0,slice_n+1,2):
      # print(f"======= f{i}")
      if i+1 > slice_n:
        answer += arr[i]
        break
      if arr[i]*arr[i+1] < 0:
        answer += arr[i]+arr[i+1]
      else:
        answer += arr[i]*arr[i+1]
  
  print(answer)