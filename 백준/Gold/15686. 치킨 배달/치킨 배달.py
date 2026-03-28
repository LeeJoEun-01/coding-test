import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
maps = []

chic = []
home = []
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        if line[j] == 2:
            chic.append([i, j])
        elif line[j] == 1:
            home.append([i, j])


def calc_dis(chics):
    sum = 0
    for i in range(len(home)):
        tmp = []
        target = home[i]
        for c in chics:
            tmp.append(abs(c[0]-target[0])+abs(c[1]-target[1]))
        sum += min(tmp)

    return sum


# 치킨집 콤비네이션
result = []
for com in combinations(chic, M):
    # 치킨 거리 합 구한는 함수
    dis = calc_dis(com)
    result.append(dis)

print(min(result))