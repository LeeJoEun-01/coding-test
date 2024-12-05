import sys
import heapq

N = int(sys.stdin.readline().rstrip())
arr = []

for _ in range(N):
  a, b = map(int, sys.stdin.readline().split())
  arr.append([a,b])

arr.sort(key = lambda x: x[0])
heap = []

heapq.heappush(heap, arr[0][1])

for i in range(1,len(arr)):
  if arr[i][0] >= heap[0]:
    heapq.heappop(heap)
  heapq.heappush(heap, arr[i][1])

print(len(heap))
