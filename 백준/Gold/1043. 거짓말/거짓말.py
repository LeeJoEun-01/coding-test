import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
truth = list(map(int, sys.stdin.readline().rstrip().split()))
party = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(M)]
result = []

def find(parent,x):
  if x != parent[x]:
    parent[x] = find(parent, parent[x])
  return parent[x]

def union(parent,a,b):
  a = find(parent,a)
  b = find(parent,b)
  
  if a<b:
    parent[b]=a
  else:
    parent[a]=b

parent = [i for i in range(N+1)]
count = M

if truth[0] == 0:
  print(M)
else:
  del truth[0]
  truth = set(truth)

  for i in range(M):
    arr = sorted(party[i][1:])
    for j in range(1,len(arr)):
      if find(parent, arr[0]) != find(parent, arr[j]):
        union(parent, arr[0],arr[j])
    
  visited = [0]*(N+1)
  for i in range(1, N+1):
    if i in truth and not visited[i]:
      p = find(parent,i) 
      for j in range(1, N+1):
        if find(parent,j) == p:
          visited[j] = 1
          truth.add(j)
  
  for i in range(M):
    for j in range(1, party[i][0]+1):
      if party[i][j] in truth:
        count -= 1
        break
  print(count)