import sys

nums = sys.stdin.readline().rstrip()
target = 0
index = 0

while True:
    index += 1
    for s in str(index):
        if nums[target] == s:
            target += 1
            if target >= len(nums):
                print(index)
                exit()