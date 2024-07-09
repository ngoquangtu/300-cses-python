# A number spiral is an infinite grid whose upper-left square has number 1. Here are the first five layers of the spiral:

# Your task is to find out the number in row y and column x.
# Input
# The first input line contains an integer t: the number of tests.
# After this, there are t lines, each containing integers y and x.
# Output
# For each test, print the number in row y and column x.
# Constraints

# 1 \le t \le 10^5
# 1 \le y,x \le 10^9

# Example
# Input:
# 3
# 2 3
# 1 1
# 4 2

# Output:
# 8
# 1
# 15
# import sys
# input = sys.stdin.read
# def calculate (y,x):
#     layer=max(y,x)
#     if (layer%2==1):
#         start_number=(2*layer-1)**2+1
#         if y==layer:
#             return start_number+(x-1)
#         else: 
#             return start_number +(layer-1)+ ( layer-y)
#     else:
#         start_number=(2*layer)**2+1
#         if x==layer:
#             return start_number+(y-1)
#         else:
#             return start_number +(layer-1)+(layer-x)
# data = input().strip().split()  
# t = int(data[0])
# results = []

# index = 1
# for _ in range(t):
#     y = int(data[index])
#     x = int(data[index + 1])
#     results.append(calculate(y, x))
#     index += 2
# for result in results:
#     print(result)
import sys
input = sys.stdin.read

def find_number_in_spiral(y, x):
    layer = max(y, x)  # Determine the layer which contains (y, x)
    if layer % 2 == 1:
        # Odd layer
        start_number = (2 * layer - 1) ** 2 + 1
        if y == layer:
            return start_number + (x - 1)
        else:
            return start_number + (layer - 1) + (layer - y)
    else:
        # Even layer
        start_number = (2 * layer) ** 2 + 1
        if x == layer:
            return start_number + (y - 1)
        else:
            return start_number + (layer - 1) + (layer - x)

import sys
input = sys.stdin.read

# Reading input
data = input().strip().split()
t = int(data[0])
results = []

index = 1
for _ in range(t):
    y = int(data[index])
    x = int(data[index + 1])
    results.append(find_number_in_spiral(y, x))
    index += 2

# Printing results
for result in results:
    print(result)


        

