import sys
input = sys.stdin.readline
allGrant = 0.0
total = 0.0

for _ in range(20):
    name, grant, alpha = map(str, input().split())
    num = 0
    if alpha != "P":
        allGrant += float(grant)

        if alpha == "A+":
            num = 4.5
        elif alpha == "A0":
            num = 4.0
        elif alpha == "B+":
            num = 3.5
        elif alpha == "B0":
            num = 3.0
        elif alpha == "C+":
            num = 2.5
        elif alpha == "C0":
            num = 2.0
        elif alpha == "D+":
            num = 1.5
        elif alpha == "D0":
            num = 1.0
        elif alpha == "F":
            num = 0.0

        total += num*float(grant)

print(round(total/allGrant, 6))