#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 12904                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/12904                          #+#        #+#      #+#     #
#    Solved: 2025/05/27 09:45:15 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

S = list(input().rstrip())
T = list(input().rstrip())
isDone = False

while T:
    if T[-1] == "A":
        T.pop()
    elif T[-1] == "B":
        T.pop()
        T.reverse()

    if S == T:
        isDone = True
        break

if isDone:
    print(1)
else:
    print(0)
