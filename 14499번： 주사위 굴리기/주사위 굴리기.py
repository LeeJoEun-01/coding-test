#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14499                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14499                          #+#        #+#      #+#     #
#    Solved: 2025/03/11 20:48:12 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
inputs = list(map(int, input().split()))
dice = [0]*6

def move(num):
  if num == 1: #동쪽
    dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]
  elif num == 2: #서쪽
    dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]
  elif num == 3: #북쪽
    dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]
  else: #남쪽
    dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]

dx = [0,0,-1,1] #동서북남
dy = [1,-1,0,0]
for i in inputs:
  newX = x + dx[i-1]
  newY = y + dy[i-1]
  if 0<= newX < N and 0<= newY < M:
    x = newX
    y = newY
    move(i)
    if board[x][y] == 0:
      board[x][y] = dice[5]
    else:
      dice[5] = board[x][y]
      board[x][y] = 0
    
    print(dice[0])