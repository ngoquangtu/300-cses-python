# Your task is to calculate the number of bit strings of length n.
# For example, if n=3, the correct answer is 8, because the possible bit strings are 000, 001, 010, 011, 100, 101, 110, and 111.
# Input
# The only input line has an integer n.
# Output
# Print the result modulo 10^9+7.
# Constraints

# 1 \le n \le 10^6

# Example
# Input:
# 3

# Output:
# 8

# def calculate(n):
#     lenth=2**n
#     binary_array=[]
#     for i in range (lenth):
#         binary_number=""
#         number=i
#         for _ in range(n):
#             binary_number=str(number%2)+binary_number
#             number=number//2
        
#         while len(binary_number) < n:
#             binary_number = "0" + binary_number
#         binary_array.append(binary_number)
#     print(len(binary_array))
def calculate(n):
    MOD= 10**9+7
    result=pow(2,n,MOD)
    print(result)
n = int(input().strip())
calculate(n)
