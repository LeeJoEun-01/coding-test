from collections import deque
import math

def solution(board):
    answer = 0
    start = [0,0,0]
    nx = len(board)
    ny = len(board[0])
    dist = [[math.inf for _ in range(ny)] for _ in range(nx)]

    for i in range(nx):
        line = list(board[i])
        board[i] = line
        for j in range(ny):
            if line[j] == 'R':
                start[0] = i
                start[1] = j
                dist[i][j] = 0
                break

    queue = deque([start])

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    while queue:
        x, y, count = queue.popleft()

        if board[x][y] == "G":
            return count
        
        for i in range(4):
            newX = x
            newY = y 

            while 0 <= newX+dx[i] < nx and 0 <= newY+dy[i] < ny and board[newX+dx[i]][newY+dy[i]] != "D" :
                newX += dx[i]
                newY += dy[i]

                    
            if dist[newX][newY] > count+1:
                dist[newX][newY] = count+1
                queue.append([newX,newY,count+1])

    return -1