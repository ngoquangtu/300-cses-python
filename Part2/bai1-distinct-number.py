# You are given a list of n integers, and your task is to calculate the number of distinct values in the list.
# Input
# The first input line has an integer n: the number of values.
# The second line has n integers x_1,x_2,\dots,x_n.
# Output
# Print one integers: the number of distinct values.
# Constraints

# 1 \le n \le 2 \cdot 10^5
# 1 \le x_i \le 10^9

# Example
# Input:
# 5
# 2 3 2 2 3

# Output:
# 2

def calculate(n, array):
    array.sort()
    set1 = set()
    i = 0
    while i < n:
        if i < n - 1 and array[i] == array[i + 1]:
            if(array[i] not in set1):
                set1.add(array[i])
            i += 2
     
        else:
            set1.add(array[i])
            i += 1
    print(len(set1) or 1)
n=int(input().strip())
array = list(map(int, input().strip().split()))
calculate(n,array)