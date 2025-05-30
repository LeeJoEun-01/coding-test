import sys
input = sys.stdin.readline

N = int(input().rstrip())
for _ in range(N):
    target = int(input().rstrip())
    q = 0
    d = 0
    n = 0
    p = 0
    while target > 0:
        if target >= 25:
            q += 1
            target -= 25
        elif target >= 10:
            d += 1
            target -= 10
        elif target >= 5:
            n += 1
            target -= 5
        elif target >= 1:
            p += 1
            target -= 1
    print(f"{q} {d} {n} {p}")