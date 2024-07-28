N = int(input())
meetings = []

# 입력 배열 받기
for i in range (N):
  startTime, endTime = map(int, input().split())
  meetings.append([startTime, endTime])

meetings = sorted(meetings, key=lambda x: (x[1], x[0]))


# 회의실 배정
startTime = 0
endTime = 0
result = []

for meet in (meetings):
  if meet[0] >= endTime and meet[1] >= endTime:
    startTime = meet[0]
    endTime = meet[1]
    # print(meet)
    result.append(meet)
    
  
print(len(result))
