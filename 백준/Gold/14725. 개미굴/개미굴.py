
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline


def dfs(node_dict, depth):
    for name in sorted(node_dict.keys()):
        indent = ''
        for _ in range(depth):
            indent += '--'
        print(indent + name)
        dfs(node_dict[name], depth + 1)


n = int(input().rstrip())
tree = {}

for _ in range(n):
    parts = input().split()
    cats = parts[1:]

    cur = tree
    for c in cats:
        if c not in cur:
            cur[c] = {}
        cur = cur[c]

dfs(tree, 0)
