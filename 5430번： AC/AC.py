# #  **************************************************************************  #
# #                                                                              #
# #                                                       :::    :::    :::      #
# #    Problem Number: 5430                              :+:    :+:      :+:     #
# #                                                     +:+    +:+        +:+    #
# #    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
# #                                                   +#+      +#+        +#+    #
# #    https://boj.kr/5430                           #+#        #+#      #+#     #
# #    Solved: 2024/11/27 22:30:31 by joeun1005     ###          ###   ##.kr     #
# #                                                                              #
# #  **************************************************************************  #

# import sys
# from collections import deque

# N = int(sys.stdin.readline().rstrip())

# for _ in range(N):
#   commands = list(sys.stdin.readline().rstrip())
#   n = int(sys.stdin.readline().rstrip())
#   arr = sys.stdin.readline().rstrip()[1:-1].split(",")

#   if n == 0:
#     arr = []

#   start = 0
#   queue = deque(arr)
#   result = True
#   rCount = 0

#   for command in commands:
#     if command == 'R':
#       rCount += 1
#     elif command == 'D':
#       if queue:
#         if rCount%2 == 0:
#           queue.popleft()
#           rCount = 0
#         else:
#           queue.pop()
#           rCount = 1
#       else:
#         result = False
  
#   if rCount%2 != 0:
#     queue.reverse()

#   if result == False :
#     print("error")
#   else:
#     print("[" + ",".join(queue) + "]")

# [PCCP 기출문제] 3번.  충돌위험 찾기
def findRoutes(points):
    results = []
    r = points[0][0]
    c = points[0][1]
    
    for i in range(1,len(points)):
        if i == 1:
            line = [[r,c]]
        else:
            line = []

        endR = points[i][0]
        endC = points[i][1]
        
        while r != endR or c != endC:
            if r > endR:
                r -= 1
            elif r < endR:
                r += 1
            else:
                if c > endC:
                    c -= 1
                elif c < endC:
                    c += 1
                else:
                    break
            
            line.append([r,c])            
        results += line
    
    return results
    

def solution(points, routes):
    answer = 0
    result = []
    lens = []
    
    for line in routes:
        arr = []
        for v in line:
            arr.append(points[v-1])
        
        tmp = findRoutes(arr)
        result.append(tmp)
        lens.append(len(tmp))

    # print(f"=== result: {result}")

    for j in range(max(lens)):
        target = []
        notTarget = []
        for i in range(len(routes)):
            if lens[i] > j:
                # print(f"🌟===: i: {i} | j:{j}  = {result[i][j]}")
                if result[i][j] in target:
                    # print(f"===: i: {i} | j:{j}  = {result[i][j]}")
                    target.remove(result[i][j])
                    if result[i][j] not in notTarget:
                        answer += 1
                    notTarget.append(result[i][j]) 
                target.append(result[i][j])
    
    return answer
  
print(solution([[1, 1], [2, 2], [3, 3]], [[1, 2, 1], [3, 2, 1]]))