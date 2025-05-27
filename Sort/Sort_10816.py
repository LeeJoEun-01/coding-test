# Sort
# 10816, 숫자 카드 2

import sys
from collections import Counter

n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))

n_dic = Counter(n_list)

# print(n_dic)

for i in m_list:
    print(n_dic[i], end=" ")
