
import sys
import math
input = sys.stdin.readline

H, W, N, M = map(int, input().split())

col = math.ceil(H/(N+1))
row = math.ceil(W/(M+1))

print(col*row)