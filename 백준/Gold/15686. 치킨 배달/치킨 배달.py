import sys

N, M = map(int, sys.stdin.readline().split())
house = []
chicken = []

for i in range(N):
  input = list(map(int, sys.stdin.readline().split()))
  for j in range(N):
    if input[j] == 1:
      house.append([i,j])
    elif input[j] == 2:
      chicken.append([i,j])       

def calcTotalDistance(house, chicken):
  totalDistance = 0
  for ho in house:
     minDistance = 999999
     for ch in chicken:
        distance = calcDistance(ho,ch)
        distance = abs(ho[0]-ch[0]) + abs(ho[1]-ch[1])
        if minDistance > distance:
          minDistance = distance
     totalDistance = totalDistance + minDistance
  return totalDistance

def calcDistance(aHouse, aChicken):
  distance = abs(aHouse[0]-aChicken[0]) + abs(aHouse[1]-aChicken[1])
  return distance

candidate = []
dfsDistance = 999999

def dfs(startIndex):
  global dfsDistance

  if len(candidate) == M:
    totalDistance = calcTotalDistance(house, candidate)
    if dfsDistance > totalDistance:
      dfsDistance = totalDistance
    return
   
  for i in range(startIndex, len(chicken)+1):
      candidate.append(chicken[i-1])
      startIndex += 1
      dfs(startIndex)
      candidate.pop()
  
  return dfsDistance

   
startIndex = 1

if M == len(chicken):
   print(calcTotalDistance(house, chicken))
else:
   print(dfs(startIndex))