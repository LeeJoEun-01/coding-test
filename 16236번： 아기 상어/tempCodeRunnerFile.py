
# def bfs(x,y):
#   visited = [[0]*N for _ in range(N)]
#   queue = deque([x,y])
#   candidates = []

#   visited[x][y] = 1

#   while queue:
#     i, j = queue.popleft()

#     for d in range(4):
#       newI = i + dx[d]
#       newJ = j + dy[d]

#       if newI >= 0 and newI < N and newJ >= 0 and newJ < N and visited[newI][newJ] == 0:
#         if arr[x][y] > arr[newI][newJ] and arr[newI][newJ] != 0:
#           visited[newI][newJ] = visited[i][j] + 1
#           candidates.append([visited[newI][newJ]-1, newI, newJ])
#         elif arr[x][y] == arr[newI][newJ]:
#           visited[newI][newJ] = visited[i][j] + 1
#           queue.append([newI, newJ])
#         elif arr[newI][newJ] == 0:
#           visited[newI][newJ] = visited[i][j] + 1
#           queue.append([newI, newJ])

#   return sorted(candidates, key = lambda x: (x[0], x[1], x[2]))

# count = 0
# size = [2,0]