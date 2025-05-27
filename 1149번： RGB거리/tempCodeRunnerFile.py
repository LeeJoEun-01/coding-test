
# def dp(i):
#   color = 0
#   min_value = min(arr[i])
#   color = arr[i].index(min)
#   arr[i][color] = 1001

#   return color, min_value

# for i in range(N):
#   current_color, value = dp(i)
#   if prev_color == current_color:
#       current_color, value = dp(i)
#   prev_color = current_color
#   sum += value

# print(sum)