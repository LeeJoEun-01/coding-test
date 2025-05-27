#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2503                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joeun1005 <boj.kr/u/joeun1005>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2503                           #+#        #+#      #+#     #
#    Solved: 2025/01/06 20:30:29 by joeun1005     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


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
            count += 1
            return
        else:
            for i in range(n):
                print(f"=== {row},{i}")
                cols[row] = i
                if promising(row):
                    print(f"{row},{i}")
                    dfs(row+1)
        
    dfs(0)
    return count

print(solution(4))