# A Gray code is a list of all 2^n bit strings of length n, where any two successive strings differ in exactly one bit (i.e., their Hamming distance is one).
# Your task is to create a Gray code for a given length n.
# Input
# The only input line has an integer n.
# Output
# Print 2^n lines that describe the Gray code. You can print any valid solution.
# Constraints

# 1 \le n \le 16

# Example
# Input:
# 2

# Output:
# 00
# 01
# 11
# 10

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
#     for i in binary_array:
#         print(i)

def calculate(n):
    length = 2 ** n
    
    for i in range(length):
        gray_code = i ^ (i >> 1)  # Tính toán Gray code cho số nguyên i
        
        # Tạo chuỗi nhị phân từ gray_code
        binary_number = ""
        for j in range(n):
            bit_value = (gray_code >> (n - 1 - j)) & 1  # Lấy giá trị của bit thứ j từ phải sang trái
            binary_number += str(bit_value)
        
        print(binary_number)
n=int(input().strip())
calculate(n)