import sys

N, r, c = map(int, sys.stdin.readline().split())
count = 0

def find(x,y,n):
  global count
  if x>r or x+n <= r or y>c or y+n <= c:
    count += n**2
    return 
  
  if n > 2:
    n = n//2
    find(x,y,n)
    find(x,y+n,n)
    find(x+n,y,n)
    find(x+n,y+n,n)
  else:
    if x == r and y == c:
      print(count)
    elif x == r and y+1 == c:
      print(count+1)
    elif x+1 == r and y == c:
      print(count+2)
    else:
      print(count+3)
    return 
  
find(0,0,2**N)