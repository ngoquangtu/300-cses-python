# Given a string, your task is to reorder its letters in such a way that it becomes a palindrome (i.e., it reads the same forwards and backwards).
# Input
# The only input line has a string of length n consisting of characters A–Z.
# Output
# Print a palindrome consisting of the characters of the original string. You may print any valid solution. If there are no solutions, print "NO SOLUTION".
# Constraints

# 1 \le n \le 10^6

# Example
# Input:
# AAAACACBA

# Output:
# AACABACAA

# def calculate(s):
#     array=list(s)
#     result=[]
#     left=0
#     right=len(array)-1
#     check=0
#     for i in range (len(array)):
#         count=0
#         for j in range (len(array)):
#             if array[i]==array[j]:
#                 count=count+1
#         if(count%2==1):
#             check+=1
#             if(check >=2):
#                 print("NO SOLUTION")
#                 return    
#     while left<=right:
#         result.append(array[left])
#         array[left]=array[right]
#         array[right]=result[left]
#         left=left+1
#         right=right-1
#         array[left]
#     result="".join(array)
#     print(result)
def calculate(s):
    freq = {}
    check = []
    
    # Đếm tần số xuất hiện của mỗi ký tự
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1   
    
    # Kiểm tra có quá nhiều ký tự có số lần xuất hiện lẻ hay không
    for count in freq.values():
        if count % 2 != 0:
            check.append(count)
        if len(check) >= 2:
            print("NO SOLUTION")
            return
    
    half_left = []

    middle_char = []
    
    # Xây dựng nửa chuỗi trái và nửa chuỗi phải của palindrome
    for char, count in freq.items():
        if count % 2 == 0:
            half_left.extend([char] * (count // 2))

        else:
            middle_char.append(char*count) # Lưu ký tự xuất hiện số lần lẻ
    
    # # Xử lý ký tự xuất hiện số lần lẻ
    # if len(check) == 1:
    #     middle_char.append(char)
    
    # Tạo chuỗi palindrome từ các nửa và ký tự giữa
    result = ''.join(half_left) + ''.join(middle_char) + ''.join(reversed(half_left))
    print(result)

s=str(input().strip())
calculate(s)

