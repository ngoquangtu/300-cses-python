# Your task is to calculate the number of trailing zeros in the factorial n!.
# For example, 20!=2432902008176640000 and it has 4 trailing zeros.
# Input
# The only input line has an integer n.
# Output
# Print the number of trailing zeros in n!.
# Constraints

# 1 \le n \le 10^9

# Example
# Input:
# 20

# Output:
# 4

# def calculate(n):
#     result=1
#     count=0
#     maxcount=0

#     for i in range(1,n+1):
#         result=i*result
#     result=str(result)
#     length=len(result)
#     for i in range(length):
#         if(result[i]=="0"):
#             count=count+1
#             maxcount=max(count,maxcount)
#         else:
#             count=0
#     print(maxcount)
def calculate(n):
    count = 0
    i = 5
    while n // i >= 1:
        count += n // i
        i *= 5
    print(count)
n = int(input().strip())
calculate(n)