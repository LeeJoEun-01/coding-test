import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(R)]
cleaner_pos = []
for r in range(R):
    if maps[r][0] == -1:
        cleaner_pos.append(r)

# 공기청정기 위쪽, 아래쪽 행 좌표
up_cleaner_r = cleaner_pos[0]
down_cleaner_r = cleaner_pos[1]

# 미세먼지 확산 함수


def spread_dust():
    # 확산은 '동시에' 일어나므로, 변경될 값을 저장할 새 배열이 필요
    new_maps = [[0] * C for _ in range(R)]
    # 공기청정기 위치는 미리 표시
    new_maps[up_cleaner_r][0] = -1
    new_maps[down_cleaner_r][0] = -1

    # 상, 하, 좌, 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for r in range(R):
        for c in range(C):
            if maps[r][c] > 0:
                spread_amount = maps[r][c] // 5
                spread_count = 0

                for i in range(4):
                    nr, nc = r + dr[i], c + dc[i]

                    if 0 <= nr < R and 0 <= nc < C and maps[nr][nc] != -1:
                        new_maps[nr][nc] += spread_amount
                        spread_count += 1

                new_maps[r][c] += maps[r][c] - (spread_amount * spread_count)

    return new_maps

# 위쪽 공기청정기 작동 (반시계)


def run_up_cleaner():
    # 1. 아래 -> 위
    for r in range(up_cleaner_r - 1, 0, -1):
        maps[r][0] = maps[r-1][0]
    # 2. 왼쪽 -> 오른쪽
    for c in range(C - 1):
        maps[0][c] = maps[0][c+1]
    # 3. 위 -> 아래
    for r in range(up_cleaner_r):
        maps[r][C-1] = maps[r+1][C-1]
    # 4. 오른쪽 -> 왼쪽
    for c in range(C - 1, 1, -1):
        maps[up_cleaner_r][c] = maps[up_cleaner_r][c-1]

    # 공기청정기에서 나온 바람은 정화됨
    maps[up_cleaner_r][1] = 0

# 아래쪽 공기청정기 작동 (시계)


def run_down_cleaner():
    # 1. 위 -> 아래
    for r in range(down_cleaner_r + 1, R - 1):
        maps[r][0] = maps[r+1][0]
    # 2. 왼쪽 -> 오른쪽
    for c in range(C - 1):
        maps[R-1][c] = maps[R-1][c+1]
    # 3. 아래 -> 위
    for r in range(R - 1, down_cleaner_r, -1):
        maps[r][C-1] = maps[r-1][C-1]
    # 4. 오른쪽 -> 왼쪽
    for c in range(C - 1, 1, -1):
        maps[down_cleaner_r][c] = maps[down_cleaner_r][c-1]

    maps[down_cleaner_r][1] = 0


for _ in range(T):
    maps = spread_dust()
    run_up_cleaner()
    run_down_cleaner()

# 최종 미세먼지 양 계산
total_dust = 0
for r in range(R):
    for c in range(C):
        if maps[r][c] > 0:
            total_dust += maps[r][c]

print(total_dust)
