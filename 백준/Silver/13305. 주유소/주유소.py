import sys
input = sys.stdin.readline

N = int(input().rstrip())
dis = list(map(int, input().split()))
cost = list(map(int, input().split()))

answer = 0
min_cost = 0

for i in range(N-1):
  if min_cost == 0:
    min_cost = cost[i]
    answer += dis[i]*cost[i]
  else:
    if min_cost > cost[i]:
      min_cost = cost[i]
    answer += dis[i]*min_cost

print(answer)