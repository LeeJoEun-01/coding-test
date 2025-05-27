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
from collections import deque
input = sys.stdin.readline

S = list(input().rstrip())
T = list(input().rstrip())

nS = len(S)
nT = len(T)
aCounting = T.count("A")

deq = deque([S])
count = 0
result = []
while deq:
    target = deq.popleft()
    # print(f"= target: {target}")
    if len(target) == nT:
        result.append(target)

    if target.count("A") < aCounting:
        addA = target[:]
        addA += "A"
        deq.append(addA)
    if target.count("B") < nT-aCounting:
        reverseB = target[::-1]
        reverseB += "B"
        deq.append(reverseB)
    #     print(f"= target: {target}")
    # print(f"== target: {target} | deq: {deq}")

ans = 0
if T in result:
    ans = 1
print(ans)
