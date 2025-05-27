#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11054                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11054                          #+#        #+#      #+#     #
#    Solved: 2025/05/11 15:58:31 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = list(map(int, input().split()))
re_arr = list(reversed(arr))

increase = [1]*N
decrease = [1]*N

for i in range(N):
    for j in range(i):

        if arr[i] > arr[j]:
            increase[i] = max(increase[i], increase[j]+1)

        if re_arr[i] > re_arr[j]:
            decrease[i] = max(decrease[i], decrease[j]+1)

decrease.reverse()

ans = 0
for i in range(N):
    s = increase[i]+decrease[i]-1
    if ans < s:
        ans = s

print(ans)
