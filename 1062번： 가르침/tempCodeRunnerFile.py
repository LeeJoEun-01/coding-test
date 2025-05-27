import sys
input = sys.stdin.readline

N, K = map(int, input().split())
words = [ input().rstrip() for _ in range(N)]
know = ['a','n','t','i','c']

answer = 0
num = 0
tmp = []

for i in range(N):
  words[i] = list(set(words[i][4:-4])-set(know))

def counting():
  global tmp
  count = 0
  for word in words:
    if all(char in tmp for char in word):
        count += 1
        
  return count

def backTracking(start, depth):
  global answer
  len_tmp = len(tmp)
  if len_tmp > num:
    return
  if depth == K - 5:
    answer = max(answer, counting())
    
  for i in range(start, N):
    tmp.extend(words[i])
    backTracking(i+1, depth+1)
    for _ in range(len(words[i])):
      tmp.pop()

if K < 5:
  print(0)
else:
  num = K-5
  for i in range(0, num+1):
    n = i
    backTracking(0,0)
  print(answer)