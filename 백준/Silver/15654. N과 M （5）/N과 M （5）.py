import sys
from itertools import *

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

result = list(permutations(arr, M))

for row in result:
  for ele in row:
    print(ele, end=" ")
  print()