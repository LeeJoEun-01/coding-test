import sys
N = int(sys.stdin.readline().rstrip())

board = [0]*N # 일차원 배열, 어차피 한 줄에 하나만 존재할 수 있다.
cnt = 0

def check(x):
  for i in range(x):
    if board[x] == board[i] or x-i == abs(board[x]-board[i]):
      return False
  return True

def backTracking(x):
  global cnt

  if x == N:
    cnt += 1
    return
  
  else:
    for i in range(N):
      board[x] = i
      if check(x):
        backTracking(x+1)

backTracking(0)
print(cnt)