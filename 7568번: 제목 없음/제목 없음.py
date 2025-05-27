#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 7568                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/7568                           #+#        #+#      #+#     #
#    Solved: 2025/05/20 20:21:32 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

N = int(input())
inputs = []

for i in range(N):
    w, h = map(int, input().split())
    inputs.append((i, w, h))

# ※ 키 기준 정렬은 제거했습니다.
# inputs.sort(key=lambda x: x[2])

ans = [0] * N
for i in range(N):
    count = 0
    # j도 0..N-1 전체를 비교
    for j in range(N):
        # 둘 다 strictly greater 여야만 count 증가
        if inputs[i][1] < inputs[j][1] and inputs[i][2] < inputs[j][2]:
            count += 1
    ans[inputs[i][0]] = count + 1

print(*ans)
