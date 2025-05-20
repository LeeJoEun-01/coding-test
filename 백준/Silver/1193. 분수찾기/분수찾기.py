
import sys

N = int(sys.stdin.readline().rstrip())
count = 1
x, y = 1, 1

# 오른쪽, 대각선 아래,아래, 대각선 위
d_index = 0
d = [[0, 1], [1, -1], [1, 0], [-1, 1]]
go = True

while count < N:

    x += d[d_index][0]
    y += d[d_index][1]

    if x == 1 or y == 1:
        d_index += 1
        d_index %= 4

    count += 1

print(f"{x}/{y}")