import sys

input = sys.stdin.readline
N, C = map(int, input().split())
arr = [ int(input().rstrip()) for _ in range(N) ]

arr.sort()

start = 1
end = arr[N-1]-arr[0]
result = 0

while start <= end :
  mid = (start+end)//2
  
  location = arr[0]
  count = 1
  for i in range(1,N):
    if arr[i]-location >= mid:
      count += 1
      location = arr[i]
  
  if count >= C:
    result = mid
    start = mid + 1
  else:
    end = mid-1

print(result)