# DP
# 1149. RGB거리

import sys

n = int(sys.stdin.readline())

cost_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

min_cost = min(cost_list)
min_index = cost_list.index(min_cost)

cost_list[min_cost][0] = 1000


print(min_index)
