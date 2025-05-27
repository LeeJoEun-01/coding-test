#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1912                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1912                           #+#        #+#      #+#     #
#    Solved: 2025/05/12 20:11:25 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = list(map(int, input().split()))
result = []
ans = 0

for i in range(N):
    if arr[i] > ans+arr[i]:
        ans = arr[i]
    else:
        ans += arr[i]
    result.append(ans)
#     print(f"=== i: {i} | ans: {ans}")

# print(result)
print(max(result))
