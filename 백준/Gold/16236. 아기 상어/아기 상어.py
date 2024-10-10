import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
arr = []
shark = []
for i in range(N):
  line = list(map(int, sys.stdin.readline().split()))
  if 9 in line:
    index = line.index(9)
    shark = [i, index]
  arr.append(line)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x,y):
  visited = [[0]*N for _ in range(N)]
  queue = deque([[x,y]])
  candidates = []

  while queue:
    i, j = queue.popleft()

    for d in range(4):
      newI = i + dx[d]
      newJ = j + dy[d]

      # 배열 크기 안에 존재하는 지와 방문했는지를 체크
      if newI >= 0 and newI < N and newJ >= 0 and newJ < N and visited[newI][newJ] == 0:
        # 상어가 물고기 보다 크고, 0이 아니면 => 상어가 먹이를 먹을 수 있음
        if arr[x][y] > arr[newI][newJ] and arr[newI][newJ] != 0:
          visited[newI][newJ] = visited[i][j] + 1
          candidates.append([visited[newI][newJ], newI, newJ])
        # 상어 크기와 물고기 크기가 같다면 => 지나갈 수 있음
        elif arr[x][y] == arr[newI][newJ]:
          visited[newI][newJ] = visited[i][j] + 1
          queue.append([newI, newJ])
        # 0이면 => 지나갈 수 있음
        elif arr[newI][newJ] == 0:
          visited[newI][newJ] = visited[i][j] + 1
          queue.append([newI, newJ])

  # 후보들을 조건에 맞춰서 정렬
  # 자나가야하는 칸의 개수의 최솟값 > 가장 위에 있는 물고기 > 가장 왼쪽에 있는 물고기
  return sorted(candidates, key = lambda x: (x[0], x[1], x[2]))

count = 0
i, j = shark[0], shark[1]
size = [2,0]

while True:
  arr[i][j] = size[0]
  candidates = deque(bfs(i, j))

  # print(f"=== candidates: {candidates}")

  if not candidates:
    break

  step, xx, yy = candidates.popleft()
  count += step # 거리
  size[1] += 1 # 먹이

  # print(f"==== count: {count}")

  # 상어 크기 업데이트
  if size[0] == size[1]:
    size[0] += 1
    size[1] = 0

  arr[i][j] = 0
  i, j = xx, yy

print(count)