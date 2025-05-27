#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1759                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1759                           #+#        #+#      #+#     #
#    Solved: 2025/05/03 16:34:49 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

# 모음
vowels = ['a', 'e', 'i', 'o', 'u']

L, C = map(int, sys.stdin.readline().split())
inputs = list(map(str, sys.stdin.readline().split()))
ans = []
inputs.sort()


def backTracking(start, vol_n, con_n):

    if len(ans) == L:
        if vol_n >= 1 and con_n >= 2:
            print(''.join(ans))
        return

    for i in range(start, C):
        c = inputs[i]
        if c not in ans:
            # print(f"== c: {c} | ans: {ans}")
            ans.append(c)
            if c in vowels:
                backTracking(i, vol_n+1, con_n)
            else:
                backTracking(i, vol_n, con_n+1)
            ans.pop()


backTracking(0, 0, 0)
