import sys

N = int(sys.stdin.readline().rstrip())
index_arr = list(map(int, sys.stdin.readline().split()))
delete_num = int(sys.stdin.readline().rstrip())
nums = [delete_num]
visited = []
tree = [[] for i in range(N)]
root = 0 # 루트 노드

for i in range(0,N):
  if index_arr[i] == -1:
    root = i
    visited.append(i)
  else:
    if i not in nums:
      index = index_arr[i]
      if index in nums:
        nums.append(i)
      else: 
        visited.append(i)
        tree[index].append(i)

leaf_node_count = 0

# print(visited)
# print(tree)

def dfs(root):
  global leaf_node_count
  find_index = visited.index(root)
  visited[find_index] = 0
  if tree[root] == []:
    # print(f"leaf node: {index}")
    leaf_node_count += 1
  else:
    for i in tree[root]:
      if i in visited:
        dfs(i)

if delete_num != root:
  dfs(root)

print(leaf_node_count)