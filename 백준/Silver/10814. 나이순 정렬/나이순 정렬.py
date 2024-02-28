import sys

n = int(sys.stdin.readline())
member_list = []

for _ in range(n):
    age, name = sys.stdin.readline().split()
    member_list.append([int(age), name])

member_list.sort(key=lambda x: int(x[0]))

# print(sorted_dict)

for member in member_list:
    print(f"{member[0]} {member[1]}")