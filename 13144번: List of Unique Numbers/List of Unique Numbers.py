#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 13144                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/13144                          #+#        #+#      #+#     #
#    Solved: 2025/04/30 10:19:14 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input().rstrip())
inputs = list(map(int, input().split()))

answer = 0
start = 0
end = 0
tmp = []
dic = defaultdict(int)

while end < N:
    if dic[inputs[end]] == 0:
        dic[inputs[end]] += 1
        # print(f"end: {end} | start: {start}")
        answer += end-start+1
        end += 1
    else:
        dic[inputs[start]] -= 1
        start += 1

print(answer)
