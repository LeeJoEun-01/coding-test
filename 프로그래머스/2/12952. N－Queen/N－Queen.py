def solution(n):
    global count
    count = 0
    cols = [0]*n
    
    def promising(row):
        for b_row in range(row):
            # 가로, 세로, 대각선 검사
            if cols[b_row] == cols[row] or abs(cols[b_row]-cols[row])==abs(b_row-row):
                return False
        return True
    
    def dfs(row):
        global count
        
        if row == n:
            row = 0
            count += 1
            return
        else:
            for i in range(n):
                cols[row] = i
                if promising(row):
                    dfs(row+1)
        
    dfs(0)
    return count