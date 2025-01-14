import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key= lambda x:x[0])

min_num  = float("inf")
count = 0
answer = 0
answer_arr = []

for d, w in arr:
  if d > count:
    count += 1
    # print(f"==== d:{d} | count:{count} | w:{w}")
    answer += w
    answer_arr.append(w)
    if w < min_num:
      min_num = w
  else:
    if w > min_num:
      if d > count-1:
        # print(f"= d:{d} | count:{count-1} | w:{w}")
        answer -= min_num
        answer += w
        answer_arr.remove(min_num)
        answer_arr.append(w)
        min_num = min(answer_arr)

print(answer)
