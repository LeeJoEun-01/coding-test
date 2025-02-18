import sys
input = sys.stdin.readline

N, K = map(int, input().split())
words = [ input().rstrip() for _ in range(N)]
know = ['a','n','t','i','c']

answer = 0
num = 0
learn = [0]*26

for i in range(N):
  words[i] = list(set(words[i][4:-4])-set(know))
for char in know:
  learn[ord(char)-ord('a')] = 1

def counting():
  global tmp
  count = 0
  for word in words:
    check = True
    for w in word:
      if not learn[ord(w) - ord('a')]:
        check = False
        break
    if check:
      count += 1
        
  return count

def dfs(start, len_word):
  global answer

  if len_word == num:
    answer = max(answer, counting())
    return
    
  for i in range(start, 26):
    if not learn[i]:
      learn[i] = True
      dfs(i, len_word+1)
      learn[i] = False

if K < 5:
  print(0)
elif K == 26:
  print(N)
else:
  num = K-5
  dfs(0,0)
  print(answer)
