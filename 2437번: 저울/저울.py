#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2437                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2437                           #+#        #+#      #+#     #
#    Solved: 2025/05/26 15:56:55 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = list(map(int, input().split()))

arr.sort()
maxN = arr[0]
nums = [arr[0]]
isDone = False

if arr[0] == 1:
    for i in range(1, N):
        tmp = []
        for n in nums:
            nn = n+arr[i]
            if nn > maxN:
                if nn == maxN + 1:
                    tmp.append(nn)
                    maxN = nn
                elif arr[i] == maxN + 1:
                    tmp.append(arr[i])
                    maxN = arr[i]
                    if nn == maxN + 1:
                        tmp.append(nn)
                        maxN = nn
                    else:
                        isDone = True
                        break
                else:
                    isDone = True
                    break
        tmp.sort()
        nums += tmp
        if isDone:
            break
else:
    maxN = 0

print(maxN+1)
