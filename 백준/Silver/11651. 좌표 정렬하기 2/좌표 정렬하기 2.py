import sys

n = int(sys.stdin.readline())
num_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

result = sorted(num_list, key=lambda x: (x[1], x[0]))

for i in result:
    print(f"{i[0]} {i[1]}")