import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
arr = []

for i in range(N) :
    arr.append(list(input().split()))

inputs = list(input().split())

for i in inputs :
    tmp_arr = []

    if i == '1' :
        for j in range(N // 2) :
            arr[j], arr[-1-j] = arr[-1-j] , arr[j]

    if i == '2' :
        for j in range(N) :
            arr[j] = (arr[j])[::-1]
            
    if i == '3' :
        for j in range(M) :
            tmp = []
            for k in range(N-1,-1,-1) :
                tmp.append(arr[k][j])
            tmp_arr.append(tmp)
        arr = tmp_arr
        N, M = M, N

    if i == '4' :
        for j in range(M-1,-1,-1) :
            tmp = []
            for k in range(N) :
                tmp.append(arr[k][j])
            tmp_arr.append(tmp)
        arr = tmp_arr
        N, M = M, N

    if i == '5' :
        half_N, half_M = N // 2 , M // 2
        for j in range(half_N) :
            tmp_arr.append(arr[half_N + j][0:half_M] + arr[j][0:half_M])
        for j in range(half_N) :
            tmp_arr.append(arr[half_N + j][half_M:] + arr[j][half_M:])
        arr = tmp_arr

    if i == '6' :
        half_N, half_M = N // 2 , M // 2
        for j in range(half_N) :
            tmp_arr.append(arr[j][half_M :] + arr[half_N + j][half_M:])
        for j in range(half_N) :
            tmp_arr.append(arr[j][0:half_M] + arr[half_N + j][0:half_M])
        arr = tmp_arr

for i in range(N) :
    print(' '.join(arr[i]))
