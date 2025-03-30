import sys

while True:
  a, b, c = map(int, sys.stdin.readline().split())
  if a == 0 and b == 0 and c == 0:
    break

  arr = [a,b,c]
  arr.sort()

  if arr[0]+arr[1] <= arr[2]:
    print("Invalid")
  else:
    if a == b and b == c:
      print("Equilateral")
    elif a == b or b == c or a == c:
      print("Isosceles")
    else:
      print("Scalene")