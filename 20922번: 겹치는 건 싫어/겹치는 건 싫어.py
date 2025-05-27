#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 20922                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/20922                          #+#        #+#      #+#     #
#    Solved: 2025/04/27 23:38:28 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import defaultdict
input = sys.stdin.readline

N, K = map(int, input().split())
inputs = list(map(int, input().split()))
answer = 0

start = 0
end = 0

count = defaultdict(int)

while end < N:

    if count[inputs[end]] >= K:
        print(f"== input: {inputs[end]} | count: {count}")
        count[inputs[start]] -= 1
        start += 1
    else:
        print(f"== input: {inputs[end]} | count: {count}")
        count[inputs[end]] += 1
        end += 1
        answer = max(answer, end - start)

print(count)
print(answer)
