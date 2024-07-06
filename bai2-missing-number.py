# You are given all numbers between 1,2,\ldots,n except one. Your task is to find the missing number.
# Input
# The first input line contains an integer n.
# The second line contains n-1 numbers. Each number is distinct and between 1 and n (inclusive).
# Output
# Print the missing number.
# Constraints

# 2 \le n \le 2 \cdot 10^5

# Example
# Input:
# 5
# 2 3 1 5

# Output:
# 4

# def calculate(n):
#     a=[]
#     for i in range(n-2):
#         num = int(input(f"Nhập phần tử thứ {i + 1}: "))
#         a.append(num)
#     a.sort()
#     for i in range(n-2):
#         if a[i]+1==a[i+1]:
#             continue
#         else:
#             return a[i]+1
    
# calculate(5)


def calculate(n,numbers):
    sum_n=n*(n+1)//2
    sum_given=sum(numbers)
    missing_numbers=sum_n-sum_given
    return missing_numbers

n = int(input().strip())
numbers = list(map(int, input().strip().split()))
result = calculate(n,numbers)

print(result)



    