import sys
sys.setrecursionlimit(100000)

V, E = map(int, sys.stdin.readline().split())
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(E)]
parent = [x for x in range(V+1)]

edges.sort(key=lambda x:x[2])

def find_parent(x):
  if parent[x] != x:
    parent[x] = find_parent(parent[x])
  return parent[x]

def kruskal(edges):
  weight = 0

  for edge in edges:
    v1, v2, w = edge
    # print(f"{v1}  {v2}  {w}")
    # print(f"{find_parent(v1)} {find_parent(v2)}")
    num1 = find_parent(v1)
    num2 = find_parent(v2)
    if num1 != num2:
      weight += w
      if num1 < num2:
        parent[num2] = num1
      else:
        parent[num1] = num2
  return weight

print(kruskal(edges))

