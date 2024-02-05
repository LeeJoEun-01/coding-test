# Implementation
# 2108. 통계학

import sys
from collections import Counter

n = int(sys.stdin.readline())
num_list = [int(sys.stdin.readline()) for _ in range(n)]

num_list.sort()

sum_list = sum(num_list)
avg = round(sum_list/n)
middle_num = num_list[n//2]
range_num = max(num_list)-min(num_list)

counter = Counter(num_list)
max_count = max(counter.values())
many_num_arr = [num for num, count in counter.items() if count == max_count]
many_num = 0
many_num_arr.sort()
many_num = many_num_arr[0] if len(many_num_arr) == 1 else many_num_arr[1]

print(avg)
print(middle_num)
print(many_num)
print(range_num)
