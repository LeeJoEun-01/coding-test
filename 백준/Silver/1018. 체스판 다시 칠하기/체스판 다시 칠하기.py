n, m = map(int, input().split())
board = [input().rstrip() for _ in range(n)]
result = []

for i in range(n - 7):
    for j in range(m - 7):
        white_start = 0 # 흰색 시작
        black_start = 0 # 검정 시작

        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0:
                    # (짝수인 칸) B로 시작할 때 틀린 개수 ↑,
                    # W로 시작할 때 틀린 개수 ↑
                    if board[a][b] != 'B':
                        white_start += 1
                    if board[a][b] != 'W':
                        black_start += 1
                else:
                    # (홀수인 칸) 반대 색으로 시작해야 하니까 뒤집어 검사
                    if board[a][b] != 'W':
                        white_start += 1
                    if board[a][b] != 'B':
                        black_start += 1

        result.append(white_start)
        result.append(black_start)

print(min(result))