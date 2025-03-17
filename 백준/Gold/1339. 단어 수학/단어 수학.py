import sys
input = sys.stdin.readline

N = int(input().rstrip())
inputs = [ input().rstrip() for _ in range(N)]
num_arr = ['']*10
num = 9
sum = 0
dic = {}

max_len = 0
for i in inputs:
  if max_len < len(i):
    max_len = len(i)

for n in range(max_len,0,-1):
  for i in range(N):
    if len(inputs[i]) >= n:
      char = inputs[i][len(inputs[i])-n]

      if char in dic:
        dic[char] += 10**n 
      else:
        dic[char] = 10**n

sorted_dic = dict(sorted(dic.items(), key = lambda item: item[1], reverse=True))
for key in sorted_dic:
  num_arr[num] = key
  num -= 1

for i in inputs:
  len_i = len(i)
  for j in list(i):
    index_num = num_arr.index(j)
    sum += (10**(len_i-1)*index_num)
    len_i -= 1

print(sum)
