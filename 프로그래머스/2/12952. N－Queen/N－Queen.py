def solution(n):
    cols = [0]*n
    count = dfs(0, 0, cols, n)
    return count
    
def promising(row, i, cols):
    for b_row in range(row):
        # 가로, 세로, 대각선 검사
        if cols[b_row] == i or abs(cols[b_row]-i)==abs(b_row-row):
            return False
    return True

def dfs(row, cnt, cols, n):
    answer = 0
    if row == n:
        return 1
    else:
        for i in range(n):
            if promising(row, i, cols):
                cols[row] = i
                answer += dfs(row+1, cnt, cols, n)
    return answer
