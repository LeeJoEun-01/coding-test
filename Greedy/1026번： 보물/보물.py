#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1026                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1026                           #+#        #+#      #+#     #
#    Solved: 2024/08/02 17:35:39 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# 최솟값 아이디어
# 큰숫자와 작은 수자를 곱하자

N = int(input())
arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))

S = 0
arrA.sort()  # 오름차순 정렬
arrB.sort(reverse=True) # 내림차순 정렬

for i in range(N):
  S += arrA[i]*arrB[i]

print(S)