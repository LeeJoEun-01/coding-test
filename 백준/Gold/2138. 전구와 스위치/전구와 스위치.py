import sys
input = sys.stdin.readline

N = int(input().rstrip())
origin = list(map(int, input().rstrip()))
result = list(map(int, input().rstrip()))

def onOff(tmp):
  count = 0

  for _ in range(2):
    for i in range(1,N):
      if tmp[i-1] == result[i-1]:
        continue
      
      count += 1
      for j in range(i-1, i+2):
        if j < N:
          tmp[j] = 1-tmp[j]

  return count if tmp == result else 1e9

origin2 = origin[:]
cnt1 = onOff(origin)

origin2[0] = 1-origin2[0]
origin2[1] = 1-origin2[1]
cnt2 = onOff(origin2) + 1

ans = min(cnt1, cnt2)
print(ans if ans != 1e9 else -1)