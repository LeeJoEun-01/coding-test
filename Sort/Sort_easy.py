# import sys

# n = int(sys.stdin.readline())
# num_list = [int(sys.stdin.readline().strip()) for _ in range(n)]

# num_list.sort()

# for i in num_list:
#     print(i)

# 11650. 좌표 정렬하기
# import sys

# n = int(sys.stdin.readline())

# num_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# num_list.sort()

# for nums in num_list:
#     for num in nums:
#         print(num, end=" ")
#     print()

# import sys

# num_list = list(map(int, sys.stdin.readline().split()))
# num_list.sort()

# print(num_list[1])

# 10814. 나이순 정렬
# import sys

# n = int(sys.stdin.readline())
# member_list = []

# for _ in range(n):
#     age, name = sys.stdin.readline().split()
#     member_list.append([int(age), name])

# member_list.sort(key=lambda x: int(x[0]))

# # print(sorted_dict)

# for member in member_list:
#     print(f"{member[0]} {member[1]}")

# 11651. 좌표 정렬하기 2
import sys

n = int(sys.stdin.readline())
num_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

result = sorted(num_list, key=lambda x: (x[1], x[0]))

for i in result:
    print(f"{i[0]} {i[1]}")
