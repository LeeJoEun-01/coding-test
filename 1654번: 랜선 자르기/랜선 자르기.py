#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1654                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1654                           #+#        #+#      #+#     #
#    Solved: 2025/04/25 13:24:02 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
input = sys.stdin.readline

K, N = map(int, input().split())
arr = [int(input().rstrip()) for _ in range(K)]

start = 0
end = max(arr)+1
mid = (start+end)//2
answer = 0

while start < end-1:
    # print(f"=== s: {start} | mid: {mid} | e: {end}")
    mid = (start+end)//2
    count = 0

    for lan in arr:
        count += (lan//mid)

    if count < N:
        end = mid
    elif count >= N:
        start = mid
        if mid > answer:
            answer = mid

print(answer)
