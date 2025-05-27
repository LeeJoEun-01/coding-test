#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1436                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1436                           #+#        #+#      #+#     #
#    Solved: 2024/07/25 15:32:15 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N = int(input())

count = 0
num = 666

while True:
    if '666' in str(num):
        count += 1
        if N == count:
            break
    num += 1

print(num)


# 예전 풀이

# share = n // 18
# remain = n % 18

# one = 0
# last = 6


# # n이 108보다 크면
# if n >= 115 and n <= 214:
#     one = n-115
#     result = 66600+one
# else:
#     if remain <= 6 and remain > 0:
#         one = remain
#     elif remain > 6 and remain <16:
#         one = 6
#     elif remain >= 16 :
#         one = remain-9
#     elif remain == 0:
#         share -= 1
#         one = 9

#     if one == 6:
#         last = remain-6

#     result = share*10000 + one*1000 + 660 + last

# print(result)

