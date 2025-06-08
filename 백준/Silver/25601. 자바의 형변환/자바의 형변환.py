import sys
input = sys.stdin.readline

N = int(input())
dic = {}
idx = 0
parent = []

parent = [-1] * (N)

for _ in range(N-1):
    A, B = input().split()
    if A not in dic:
        dic[A] = idx
        idx += 1
    if B not in dic:
        dic[B] = idx
        idx += 1
    a = dic[A]
    b = dic[B]
    parent[a] = b

A, B = input().split()
a = dic[A]
b = dic[B]


def isAncestor(u, v):
    while v != -1:
        if v == u:
            return True
        v = parent[v]
    return False


if isAncestor(a, b) or isAncestor(b, a):
    print(1)
else:
    print(0)
