import sys

N = int(sys.stdin.readline().rstrip())
inputs = [ sys.stdin.readline().rstrip() for _ in range(N)]

KBS1_index = 0
KBS2_index = 0

for i in range(N):
  input = inputs[i]

  if input == "KBS1":
    KBS1_index = i
  elif input == "KBS2":
    KBS2_index = i

if KBS1_index > KBS2_index:
  KBS2_index += 1

print("1"*KBS1_index+"4"*KBS1_index+"1"*KBS2_index+"4"*(KBS2_index-1))