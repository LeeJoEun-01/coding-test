
import sys
input = sys.stdin.readline

M = int(input().rstrip())
S = set()
for _ in range(M):
    command = list(map(str, (input()).split()))

    if command[0] == "add":
        x = int(command[1])
        S.add(x)
    elif command[0] == "remove":
        x = int(command[1])
        if x in S:
            S.remove(x)
    elif command[0] == "check":
        x = int(command[1])
        if x in S:
            print(1)
        else:
            print(0)
    elif command[0] == "toggle":
        x = int(command[1])
        if x in S:
            S.remove(x)
        else:
            S.add(x)
    elif command[0] == "all":
        S = set([i for i in range(1, 21)])
    elif command[0] == "empty":
        S = set()
