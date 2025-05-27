# Sort
# 1744. 수 묶기
import sys

n = int(sys.stdin.readline())

num_list = [int(sys.stdin.readline().strip()) for _ in range(n)]
result_list = []

num_list.sort(reverse=True)

while (True):
    if num_list.count(0) > 0:
        for i in range(num_list.count(0)):
            last = num_list.pop()
            if last < 0:
                num_list.remove(0)
            else:
                num_list.append(last)
    # print(num_list)
    if len(num_list) == 1:
        result_list = num_list
        break

    for i in range(0, len(num_list)-1, 2):
        # print(i)
        result = num_list[i]*num_list[i+1]
        # print("i: ", num_list[i], "i+1: ", num_list[i+1])
        if result > 0:
            if num_list[i] == 1 or num_list[i+1] == 1:
                result = num_list[i]+num_list[i+1]
            result_list.append(result)
        else:
            result_list.append(num_list[i])
            result_list.append(num_list[i+1])

        if i + 2 == len(num_list)-1:
            result_list.append(num_list[i+2])
    break

# print(result_list)
print(sum(result_list))
