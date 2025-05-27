#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 15649                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/15649                          #+#        #+#      #+#     #
#    Solved: 2025/05/02 10:52:29 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

N, M = map(int, sys.stdin.readline().split())
ans = []


def backTraking():
    if len(ans) == M:
        print(*ans)
        return
    for i in range(1, N+1):
        if i not in ans:
            ans.append(i)
            backTraking()
            ans.pop()


backTraking()
